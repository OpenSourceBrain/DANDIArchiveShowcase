import os
import signal
import subprocess
import pandas as pd
import yaml
import math
import datalad.api as dl
import json
import argparse
from datetime import date
from pynwb import NWBHDF5IO
from pynwb.image import ImageSeries
from pynwb.base import TimeSeries
from pynwb.behavior import BehavioralTimeSeries, BehavioralEvents
from dandi.pynwb_utils import get_nwb_version
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import save_report, format_messages, MessageFormatter
from dandi import download
import ast

def create_dandiset_summary(args_nodownload=None,args_nosizelimit=None,args_dandisetlimit=None,
                            args_updatereadme=None,args_readmeonly=None):
    # if users want to update readme only
    if args_readmeonly:
        return args_readmeonly
    # if users want no limit on file size for downloading
    if args_nosizelimit:
        hard_limit = 100000000000
    else:
        hard_limit = 1500000000
    json_file = '.dandi/assets.json'
    # directory for dandisets
    root_folder = '/tmp/dandisets'
    if os.path.exists(root_folder):
        if len(os.listdir((root_folder))) != 0:
            dl.update(how='merge', how_subds='reset', follow='parentds-lazy', recursive=True)
        else:
            os.mkdir(root_folder)
            dl.install(source='https://github.com/dandi/dandisets.git', path=root_folder, recursive=True)
    else:
        dl.install(source='https://github.com/dandi/dandisets.git', path=root_folder, recursive=True)
    # directory for storing validation files and readme file
    save_folder = 'validation_folder'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)

    dandiset_folder_name = sorted([item for item in os.listdir(root_folder) if item.startswith('0')])

    # if user only wants to run the script for 10 dandisets
    if args_dandisetlimit:
        dandiset_folder_name = dandiset_folder_name[10:20]
    yaml_file = 'dandiset.yaml'

    yaml_df_flatten = ['identifier','citation','name','assetsSummary.numberOfBytes','assetsSummary.numberOfFiles',
                       'assetsSummary.numberOfSubjects','assetsSummary.variableMeasured','keywords','schemaKey','schemaVersion','url','version']
    tmp_col = ['species','data_type','doi_link','nwb_version','validation_summary',
               'file_size_0','file_size_1','file_0','file_1','nwbe_compatibility_0','nwbe_compatibility_1','parent_folder_0','parent_folder_1']

    dandi_metadata = pd.DataFrame()
    nanval = math.nan

    for dandiset_name in dandiset_folder_name:
        with open(os.path.join(root_folder,dandiset_name,yaml_file)) as f:
            my_dict = yaml.safe_load(f)
        # in case these variables are not available in the yaml files
        try:
            species_name = my_dict['assetsSummary']['species'][0]['name']
        except:
            species_name = nanval
        try:
            data_type = my_dict['assetsSummary']['dataStandard'][0]['name']
        except:
            data_type = nanval
        try:
            doi_link = my_dict['relatedResource'][0]['url']
        except:
            doi_link = nanval

        # flatten the yaml file and read in into dataframe
        yaml_df = pd.json_normalize(my_dict)

        # get nwb version for NWB dandisets, dummy for datasets that are not NWB
        nwb_version = nanval
        smallest_size_lst = [nanval,nanval]
        validation_summary = nanval
        url_lst = [nanval, nanval]
        file_parent_folder = [nanval,nanval]
        nwbe_compatibility = ['NI','NI']
        if data_type != nanval and 'NWB' in str(data_type):
            # get the json file that has individual files info
            with open(os.path.join(root_folder, dandiset_name, json_file)) as f:
                data = json.load(f)
            # flatten json file to pandas table
            json_df = pd.json_normalize(data)
            # sort the dataframe by column size will prevent returning series of files that have the same size
            json_df.sort_values(by='size', inplace=True)
            # get the parent folder to the file path, files to be tested should from different parent folders
            json_df['parent_folder'] = [i.split('/')[-2] for i in json_df.loc[:, 'path']]
            # there are dandisets that only have 1 file
            if len(json_df) <= 2:
                counter_i = [0, 0]
            else:
                # there are dandisets that only have 1 parent folder
                if len(json_df['parent_folder'].unique()) == 1:
                    counter_i = [1, 2]
                else:
                    for i in range(len(json_df)):
                        if json_df['parent_folder'].iloc[1] != json_df['parent_folder'].iloc[1 + i]:
                            counter_i = [1, 1 + i]
                            break
            url_lst = [json_df['metadata.contentUrl'].iloc[counter_i[0]][0],json_df['metadata.contentUrl'].iloc[counter_i[1]][0]]
            path_lst = [json_df['path'].iloc[counter_i[0]],json_df['path'].iloc[counter_i[1]]]
            smallest_size_lst = [json_df['size'].iloc[counter_i[0]],json_df['size'].iloc[counter_i[1]]]
            file_parent_folder = [json_df['parent_folder'].iloc[counter_i[0]],json_df['parent_folder'].iloc[counter_i[1]]]

            report_message = []
            # if user doesn't want to download files
            if args_nodownload:
                validation_summary = 'NOT_DOWNLOADED'
            # only download files whose sizes are lower than the hard limit
            else:
                # in case files larger than the hard_limit and not downloaded
                validation_summary = 'NULL_FILE_LIMIT'
                for i in range(len(path_lst)):
                    if smallest_size_lst[i] < hard_limit:
                        # download files
                        nwb_path = download_nwb_with_path(url_lst[i],path_lst[i])
                        # get nwb_version
                        nwb_version = get_nwb_version(nwb_path)
                        # validate file here first
                        try:
                            report_message.extend(list(inspect_nwb(nwbfile_path=nwb_path,
                                                                   importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))

                            validation_summary = nwb_inspector_message_format(report_message, dandiset_name)
                        except ValueError:
                            validation_summary = 'UNABLE'
                            pass
                        # test nwbe compatibility
                        nwbe_compatibility[i] = test_nwbe_compatibility(nwb_path)
                        print(nwbe_compatibility[i])
                        # uninstall file
                        os.unlink(nwb_path)
        # concatenate the additional variables to the flattened pdf
        yaml_df = pd.concat([yaml_df, pd.DataFrame([[species_name,data_type,doi_link,nwb_version,validation_summary,
                                                       smallest_size_lst[0],smallest_size_lst[1],url_lst[0],url_lst[1],nwbe_compatibility[0],nwbe_compatibility[1],
                                                     file_parent_folder[0],file_parent_folder[1]]],
                                                   index=yaml_df.index,columns=tmp_col)],axis=1)

        # concatenate every newly read dandiset metadata dataframe
        dandi_metadata = pd.concat([dandi_metadata,yaml_df],axis=0,ignore_index=True)
        # in case script crashes
        dandi_metadata.to_csv(os.path.join(save_folder,'dandiset_summary_tmp_tmp.csv'))
        f.close()

    # only get the relevant columns
    yaml_df_flatten.extend(tmp_col)
    dandi_metadata_final = dandi_metadata[yaml_df_flatten].sort_values(by=['identifier'],ignore_index=True)
    dandi_metadata_final.rename(columns={'assetsSummary.numberOfBytes':'num_bytes','assetsSummary.numberOfFiles':'num_files','assetsSummary.numberOfSubjects':'numb_subjects',
                                         'assetsSummary.variableMeasured':'variableMeasured', 'schemaVersion':'dandiset_schemaver'},inplace=True)
    # filter column through
    dandi_metadata_final.drop(dandi_metadata_final.filter(regex="Unnamed"), axis=1, inplace=True)
    # save table to csv
    dandi_metadata_final.to_csv(os.path.join(save_folder, 'dandiset_summary_tmp_tmp.csv'))

    # remove the cloned dandisets folder
    # dl.remove(dataset=root_folder)
    return args_updatereadme

def test_nwbe_compatibility(nwb_path):
    cmd = 'python compatibility_test.py ' + nwb_path  # the external command to run
    timeout_s = 60  # how many seconds to wait
    type_hierarchy = set([ImageSeries,TimeSeries,BehavioralTimeSeries,BehavioralEvents])
    # NC-0: file cannot be opened
    try:
        io = NWBHDF5IO(nwb_path,mode='r',load_namespaces=True)
        nwbfile = io.read()
    except:
        print('File cannot be opened - NC lvl 0')
        nwbe_compatibility = 'NC-0'
        return nwbe_compatibility
    # dummy var in case file passes NC-1 and is not a TimeSeries type
    nwbe_compatibility = 'LL-V'
    plottable = 0
    for a, v in nwbfile.acquisition.items():
        print(nwbfile.acquisition[a].neurodata_type)
        if len(set(nwbfile.acquisition[a].type_hierarchy()).intersection(type_hierarchy)) >= 1:
            if ImageSeries in nwbfile.acquisition[a].type_hierarchy():
                pass
            else:
                nwbe_compatibility = 'LL-P'
                plottable = 1
                break
    # if no TimeSeries object in acquisition module, search in processing
    if plottable == 0:
        for a, v in nwbfile.processing.items():
            print(nwbfile.processing[a].neurodata_type)
            if len(set(nwbfile.processing[a].type_hierarchy()).intersection(type_hierarchy)) >= 1:
                if ImageSeries in nwbfile.processing[a].type_hierarchy():
                    pass
                else:
                    nwbe_compatibility = 'LL-P'
                    plottable = 1
                    break
    # NC-1: timeout while creating geppetto model
    try:
        p = subprocess.Popen([cmd], start_new_session=True, shell=True)
        p.wait(timeout=timeout_s)
    except subprocess.TimeoutExpired:
        print(f'Timeout for {cmd} ({timeout_s}s) expired')
        os.killpg(os.getpgid(p.pid), signal.SIGTERM)
        nwbe_compatibility = 'NC-1'
    print('CATCH ME AGAIN')
    return nwbe_compatibility

def download_nwb_with_path(dandi_url,nwb_file_name):
    # the argument nwb_version is in case the function exits with error
    # create save folder
    save_folder = '/tmp/nwb_versions'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    if '/' in nwb_file_name:
        tmp_nwb_path = os.path.join(save_folder, nwb_file_name.split('/')[-1])
    else:
        tmp_nwb_path = os.path.join(save_folder, nwb_file_name)

    if not os.path.exists(tmp_nwb_path):
        # download 1 file here
        download.download(dandi_url, output_dir=save_folder)
    return tmp_nwb_path

def nwb_inspector_message_format(report_message,dds_id):
    save_folder = 'validation_folder'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    validation_file = os.path.join(save_folder, dds_id+'_validation.txt')
    print('Testing is finished for dandiset'+dds_id +'. report is saved as txt file.')
    save_report(report_file_path=validation_file,
                formatted_messages=format_messages(report_message, levels=['importance','file_path']),
                overwrite=True)
    # get validation types summary
    message_form = MessageFormatter(messages=report_message, levels=['file_path', 'importance'])
    validation_summary = ''
    count_tmp = 0
    for k, v in message_form.message_count_by_importance.items():
        if count_tmp == 0:
            validation_summary += k
        else:
            validation_summary += ',' + k
        count_tmp += 1
    # if a report is saved and validation_summary is not updated, its likely that no issues were found
    if os.path.exists(validation_file) and validation_summary == '':
        validation_summary = 'PASSED_VALIDATION'
    return validation_summary

def update_readme():
    save_folder = 'validation_folder'
    # rd_file = os.path.join(save_folder,'README.md')
    # summary_file = os.path.join(save_folder, 'dandiset_summary.csv')
    rd_file = os.path.join('./scratch_files','README.md')
    summary_file = os.path.join(save_folder, 'dandiset_summary_tmp_tmp.csv')
    if not os.path.exists(summary_file):
        exit()
    # Getting Datetime from timestamp
    date_time = date.today()
    dandi_metadata_readme = pd.read_csv(summary_file)
    dandi_metadata_readme.drop(dandi_metadata_readme.filter(regex="Unnamed"), axis=1, inplace=True)
    dandi_metadata_readme.to_csv(summary_file, index=False)
    print(dandi_metadata_readme)
    # summary statistics here
    data_type_dict = dandi_metadata_readme['data_type'].value_counts().to_dict()
    # get data_type values
    for k, vals in data_type_dict.items():
        if 'NWB' in k:
            nwb_type_id = k

    nwb_pd = dandi_metadata_readme.loc[dandi_metadata_readme['data_type'] == nwb_type_id].copy()
    nwb_pd.reset_index(inplace=True)
    dds_id_prefix = nwb_pd['identifier'].iloc[0].split(':')[0]
    nwb_pd.loc[:, 'identifier'] = [i.split(':')[1] for i in nwb_pd.loc[:, 'identifier']]
    pass_mwninspector = sorted([i for i in nwb_pd['identifier'].loc[(nwb_pd['validation_summary']=='BEST_PRACTICE_VIOLATION')
                                                               | (nwb_pd['validation_summary']=='PASSED_VALIDATION')]])
    nwb_pd['validation_summary'].fillna('NULL_FILE_LIMIT', inplace=True)

    readme = '# Summary statistics for the available NWB dandisets (Updated on ' + str(date_time) + ')' '\n'
    readme += '\n'
    readme += '- Total number of NWB dandisets: ' + str(data_type_dict[nwb_type_id]) + '\n'
    readme += '\n'
    readme += '- Median number of files in each NWB dandiset: ' + str(
        dandi_metadata_readme['num_files'].loc[dandi_metadata_readme.data_type == nwb_type_id].median()) + '\n'
    readme += '\n'
    readme += '- Median number of bytes in each NWB dandiset: ' + "{:,}".format(int(
        dandi_metadata_readme['num_bytes'].loc[dandi_metadata_readme.data_type == nwb_type_id].median())) + '\n'
    readme += '\n'
    readme += '- NWB dandisets that pass NWBInspector and thus are possibly NWBE compatible: '
    root_url = 'https://dandiarchive.org/dandiset/'
    for ds in pass_mwninspector:
        readme += '[%s](%s%s), '%(ds, root_url, ds)
    readme = readme[:-2]+'\n\n'

    readme += '- NWBE compatibility terminology: \n'
    readme += '  - LL-P: Likely plottable - file whose datatypes extend TimeSeries that can be viewed and plotted \n'
    readme += '  - LL-V: Likely viewable - file whose datatypes might not extend TimeSeries that can be viewed \n'
    readme += '  - NC-0: Not compatible level 0 - file cannot be opened \n'
    readme += '  - NC-1: Not compatible level 1 - geppetto model for file cannot be created \n'
    readme += '  - NI: No information - file is not tested \n\n'
    readme += '<details><summary> Summary information on the available NWB dandisets (more details in dandiset_summary.csv).\n</summary><p>'
    readme += '\n\n\n\n'

    for row in nwb_pd.index:
        ref = nwb_pd['identifier'].iloc[row]
        validation_file = ref + '_validation'
        try:
            readme += '*[DANDI:' + nwb_pd['identifier'].iloc[row] + ']' + '(' + nwb_pd['url'].iloc[
                row] + ')*' + ': **' + nwb_pd['name'].iloc[row] + '**\n\n'
        except:
            pass

        readme += '- Data type: **' + nwb_pd['data_type'].iloc[row] + '**'
        if not pd.isna(nwb_pd['nwb_version'].iloc[row]):
            readme += ' (**version ' + nwb_pd['nwb_version'].iloc[row]+'**)'

        if not pd.isna(nwb_pd['num_bytes'].iloc[row]):
            readme += ', file count: **'+str(nwb_pd['num_files'].iloc[row])+'**, total size (bytes): **' + "{:,}".format(int(nwb_pd['num_bytes'].iloc[row])) + '**\n\n'

        if not pd.isna(nwb_pd['species'].iloc[row]):
            readme += '- Species: **' + nwb_pd['species'].iloc[row] + '**\n\n'

        if not pd.isna(nwb_pd['keywords'].iloc[row]):

            kws = ast.literal_eval(nwb_pd['keywords'].iloc[row])
            if len(kws)>0:
                readme += '- Keywords: ' + ', '.join(['**%s**'%kw for kw in kws]) + '\n\n'

        if not pd.isna(nwb_pd['variableMeasured'].iloc[row]):
            vars = ast.literal_eval(nwb_pd['variableMeasured'].iloc[row])
            readme += '- Variables measured: ' + ', '.join(['**%s**'%var for var in vars])  + '\n\n'

        if not pd.isna(nwb_pd['citation'].iloc[row]):
            readme += '- Source paper: *' + nwb_pd['citation'].iloc[row].split('(Vers')[0].strip() + '*\n\n'

        if not nwb_pd['validation_summary'].iloc[row] in ['NULL_FILE_LIMIT', 'UNABLE', 'NOT_DOWNLOADED']:
            val_str = nwb_pd['validation_summary'].iloc[row].replace(',',', ')
            status = '![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png)'
            if 'PASSED_VALIDATION' in val_str:
                status = '![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png)'
            readme += '- '+status+' Validation results summary: [' + val_str + ']' + '(%s.txt) \n\n' % (validation_file)

            for i in range(2):
                if not pd.isna(nwb_pd['nwbe_compatibility_' + str(i)].iloc[row]):
                    readme += '- NWBE compatibility - file '+str(i + 1) +': ' + nwb_pd['nwbe_compatibility_' + str(i)].iloc[row] + '  \n'
                if not pd.isna(nwb_pd['file_' + str(i)].iloc[row]):
                    nwbe_link = 'http://nwbexplorer.opensourcebrain.org/hub/nwbfile=' + nwb_pd['file_' + str(i)].iloc[
                        row]
                    dandi_link = nwb_pd['url'].iloc[row] + '/files?location=' + nwb_pd['parent_folder_' + str(i)].iloc[row] +'%2F'
                    info_link = nwb_pd['file_' + str(i)].iloc[row].split('/download')[0]
                    readme += '[File info](%s) | \n' % (info_link)
                    readme += '[View on DANDI Web](%s) | \n' % (dandi_link)
                    readme += '[View on NWB Explorer](%s) \n' % (nwbe_link)

        else:
            readme += '- ![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png) Validation results summary: ' + nwb_pd['validation_summary'].iloc[row] + '\n\n'

        readme += '---'
        readme += '\n\n'
    readme += '</p></details>'
    print(readme)
    rmd = open(rd_file, 'w')
    rmd.write(readme)
    rmd.close()

if __name__ == '__main__':
    # options for users
    parser = argparse.ArgumentParser(description='cap limit on downloaded file size')
    parser.add_argument('--no_download', default=False, action='store_true',
                        help='files will not be downloaded for testing if so chosen')
    parser.add_argument('--no_sizelimit', default=False, action='store_true',
                        help='no size limit will be capped for downloading files if so chosen')
    parser.add_argument('--dandiset_limit', default=False, action='store_true',
                        help='only process first 10 dandisets if so chosen')
    parser.add_argument('--update_readme_option', default=False, action='store_true',
                        help='update readme file after summary file is created')
    parser.add_argument('--update_readme_only', default=False, action='store_true',
                        help='update readme file without creating summary file')
    args = parser.parse_args()
    update_readme_option=create_dandiset_summary(args.no_download,args.no_sizelimit,args.dandiset_limit,
                                                 args.update_readme_option,args.update_readme_only)

    if update_readme_option:
        update_readme()

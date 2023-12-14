import os
import signal
import subprocess
import pandas as pd
import yaml
import math
import datalad.api as dl
import json
import argparse
import tempfile

from datetime import date
from pynwb import NWBHDF5IO
from pynwb.image import ImageSeries
from pynwb.base import TimeSeries
from pynwb.behavior import BehavioralTimeSeries, BehavioralEvents
from dandi.pynwb_utils import get_nwb_version
from nwbinspector import inspect_nwbfile
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import save_report, format_messages, MessageFormatter
from dandi import download
import ast
from collections import Counter
from contextlib import contextmanager
from create_summary import create_summary



class TimeoutException(Exception): pass

STATUS_GREEN = '![#00dd00](https://via.placeholder.com/15/00dd00/00dd00.png)'
STATUS_AMBER = '![#ec9706](https://via.placeholder.com/15/ec9706/ec9706.png)'
STATUS_RED =   '![#dd0000](https://via.placeholder.com/15/dd0000/dd0000.png)'

@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("    ---  Timed out after %s seconds!"%seconds)
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)

def create_dandiset_summary(args_nodownload=None,args_nosizelimit=None,args_dandisetlimit=None,
                            args_updatereadme=None,args_readmeonly=None,args_testdocker=False,args_createsummary=None):
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
    if args_testdocker is False:
        if os.path.exists(root_folder):
            if len(os.listdir((root_folder))) != 0:
                dl.update(how='merge', how_subds='reset', follow='parentds-lazy', recursive=True)
            else:
                os.mkdir(root_folder)
                dl.install(source='https://github.com/dandi/dandisets.git', path=root_folder, recursive=True, recursion_limit=1, jobs=4)
        else:
            dl.install(source='https://github.com/dandi/dandisets.git', path=root_folder, recursive=True, recursion_limit=1, jobs=4)

    # directory for storing validation files and readme file
    if(args_testdocker):
        save_folder = 'testing/validation_folder'
        summary_folder = os.path.join(save_folder,'Summaries')
    else:
        save_folder = 'validation_folder'
        summary_folder = 'Summaries'
        
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
        print("\n     =================  Dealing with DANDISET ID: %s" % dandiset_name)
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
        html_info = [nanval,nanval]
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
            try:
                # get the parent folder to the file path, files to be tested should from different parent folders
                json_df['parent_folder'] = [i.split('/')[-2] for i in json_df.loc[:, 'path']]
            except IndexError:
                # in instances where a dataset has multiple parent folders but also file without a parent folder, this will apply (dandiset 29)
                json_df['parent_folder'] = nanval

            # a dataset might only have 1 file, and max_counter is the number of valid nwb files we want
            max_counter = 2
            # get the file path with the smallest size first, and check if it is a valid nwb file in the while loop
            counter = 1
            if len(json_df) == 1:
                max_counter = 1
                counter = 0
            valid_path_url = 0
            path_file = json_df['path'].iloc[counter]
            path_lst = []
            url_lst = []
            file_parent_folder = []
            smallest_size_lst = []

            while valid_path_url < max_counter:
                # check if the file with smallest file size is nwb, if not, get the next row
                if path_file.split('.')[-1] != 'nwb':
                    counter += 1
                    path_file = json_df['path'].iloc[counter]
                # if it is, return the path
                else:
                    if len(path_lst) == 1 and len(json_df['parent_folder'].unique()) != 1:
                        if file_parent_folder[0] == json_df['parent_folder'].iloc[counter]:
                            path_file = 't.blah'
                            continue
                    valid_path_url += 1
                    path_lst.append(path_file)
                    url_lst.append(json_df['metadata.contentUrl'].iloc[counter][0])
                    smallest_size_lst.append(json_df['size'].iloc[counter])
                    file_parent_folder.append(json_df['parent_folder'].iloc[counter])
                    # reinsatntiate path_file so it passes the first if
                    path_file = 't.blah'
                # in case the while loop loops through all the length of the dataframe
                if counter == len(json_df) - 1:
                    if len(url_lst) == 1:
                        url_lst.append(nanval)
                        smallest_size_lst.append(nanval)
                        file_parent_folder.append(nanval)
                        path_lst.append(nanval)
                        break
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
                            report_message.extend(list(inspect_nwbfile(nwbfile_path=nwb_path,
                                                                   importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))
                            validation_summary = nwb_inspector_message_format(report_message, dandiset_name, save_folder)      
                        except ValueError:
                            validation_summary = 'UNABLE'
                            continue
                        # test nwbe compatibility
                        if args_createsummary and not os.path.exists(os.path.join(os.path.join(summary_folder,dandiset_name),'file_'+str(i)+'/README.md')):
                            try:
                                with time_limit(300):
                                    print("   -- Creating the Summary !")
                                    create_summary(nwb_path,dandiset_name,str(i))
                            except Exception as e:
                                print("   -- Summary creation has had exception: %s"%e)

                                if os.path.exists(os.path.join(os.path.join(summary_folder,dandiset_name),'file_'+str(i)+'/README.md')):
                                    os.remove(os.path.join(os.path.join(summary_folder,dandiset_name),'file_'+str(i)+'/README.md'))
                                pass
                        nwbe_compatibility[i] = test_nwbe_compatibility(nwb_path,args_testdocker)
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
        dandi_metadata.to_csv(os.path.join(save_folder,'dandiset_summary_tmp.csv'))
        f.close()


    # only get the relevant columns
    yaml_df_flatten.extend(tmp_col)
    dandi_metadata_final = dandi_metadata[yaml_df_flatten].sort_values(by=['identifier'],ignore_index=True)
    dandi_metadata_final.to_csv(os.path.join(save_folder, 'dandiset_summary.csv')) 
    dandi_metadata_final.rename(columns={'assetsSummary.numberOfBytes':'num_bytes','assetsSummary.numberOfFiles':'num_files','assetsSummary.numberOfSubjects':'numb_subjects',
                                         'assetsSummary.variableMeasured':'variableMeasured', 'schemaVersion':'dandiset_schemaver'},inplace=True)
    
    # filter column through
    dandi_metadata_final.drop(dandi_metadata_final.filter(regex="Unnamed"), axis=1, inplace=True)
    # save table to csv
    dandi_metadata_final.to_csv(os.path.join(save_folder, 'dandiset_summary.csv'))

    # remove the cloned dandisets folder
    #dl.remove(dataset=root_folder)
    return args_updatereadme

def test_nwbe_compatibility(nwb_path,testdocker):
    if(testdocker):		
    	cmd = 'docker exec -i nwbe /bin/sh -c \'python -u testing/compatibility_test.py ' + nwb_path + ' --test_docker\''
    else:
    	cmd = 'docker exec -i nwbe /bin/sh -c \'python -u testing/compatibility_test.py ' + nwb_path + '\''
    	
    timeout_s = 60  # how many seconds to wait
    type_hierarchy = set([ImageSeries,TimeSeries,BehavioralTimeSeries,BehavioralEvents])
    
    # NC-0: file cannot be opened
    try:
        io = NWBHDF5IO(nwb_path,mode='r',load_namespaces=True)
        nwbfile = io.read()
    except:
        print('   -- File cannot be opened - NC lvl 0')
        nwbe_compatibility = 'NC-0'
        return nwbe_compatibility
        
        
    
    # dummy var in case file passes NC-1 and is not a TimeSeries type
    nwbe_compatibility = 'LL-V'
    plottable = 0
    for a, v in nwbfile.acquisition.items():
        print("   -- Type is: %s"%nwbfile.acquisition[a].neurodata_type)
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
            print("   -- Type is: %s"%nwbfile.processing[a].neurodata_type)
            if len(set(nwbfile.processing[a].type_hierarchy()).intersection(type_hierarchy)) >= 1:
                if ImageSeries in nwbfile.processing[a].type_hierarchy():
                    pass
                else:
                    nwbe_compatibility = 'LL-P'
                    plottable = 1
                    break
    # NC-1: timeout while creating geppetto model

    if(testdocker):
        with tempfile.TemporaryFile() as tempf:
                p = subprocess.Popen([cmd], start_new_session=True, shell=True, stdout=tempf)
                p.wait()
                tempf.seek(0)
                text = tempf.read()
                string_data = text.decode('utf-8')
                lower_text = string_data.lower()
                print(lower_text) #removefinal
        if "failed" in lower_text:
            nwbe_compatibility = 'NC-1'
    else:
        try:
            p = subprocess.Popen([cmd],start_new_session=True, shell=True)
            p.wait(timeout=timeout_s)
        except subprocess.TimeoutExpired:
            print(f'   -- Timeout for {cmd} ({timeout_s}s) expired')
            os.killpg(os.getpgid(p.pid),signal.SIGTERM)
            nwbe_compatibility = 'NC-1'
            
    print(nwbe_compatibility)
    return nwbe_compatibility

def download_nwb_with_path(dandi_url,nwb_file_name):
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

def nwb_inspector_message_format(report_message,dds_id,save_folder,detailed_report=None):
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    validation_file = os.path.join(save_folder, dds_id+'_validation.txt')
    print('   -- Testing is finished for Dandiset '+dds_id +'. Report is saved as txt file.')
    # if a detailed report is wanted, report will specify names of files that fail tests
    if detailed_report:
        message_levels = ['importance', 'location']
    else:
        message_levels = ['importance','file_path']
    save_report(report_file_path=validation_file,
                formatted_messages=format_messages(report_message, levels=message_levels),
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

def update_readme(testdocker=None):
    if(testdocker): 
        save_folder = 'testing/validation_folder'
        summary_folder = os.path.join(save_folder,'Summaries')
    else:
        save_folder = 'validation_folder'
        summary_folder = 'Summaries'
        
    rd_file = os.path.join(save_folder,'README.md')
    summary_file = os.path.join(save_folder, 'dandiset_summary.csv')
    
    print(summary_file)
    
    if not os.path.exists(summary_file):
        exit()
    # Getting Datetime from timestamp
    
    date_time = date.today()
    dandi_metadata_readme = pd.read_csv(summary_file)
    dandi_metadata_readme.drop(dandi_metadata_readme.filter(regex="Unnamed"), axis=1, inplace=True)
    dandi_metadata_readme.to_csv(summary_file, index=False)
    # summary statistics here
    data_type_dict = dandi_metadata_readme['data_type'].value_counts().to_dict()
    # get data_type values
    bids_exist = 0
    for k, vals in data_type_dict.items():
        if 'NWB' in k:
            nwb_type_id = k
        elif 'BIDS' in k:
            bids_type_id = k
            bids_exist = 1
        else:
            other_type_id = k

    dandi_metadata_readme.loc[:, 'identifier'] = [i.split(':')[1] for i in dandi_metadata_readme.loc[:, 'identifier']]
    nwb_pd = dandi_metadata_readme.loc[dandi_metadata_readme['data_type'] == nwb_type_id].copy()
    nwb_pd.reset_index(inplace=True)
    # get the [num_keys] most common measured variable
    num_keys = 6
    var_measured = [ast.literal_eval(i) for i in nwb_pd.loc[:, 'variableMeasured']]
    var_measured = sum(var_measured,[])
    dict_var = Counter(var_measured)
    most_common_dict = dict_var.most_common(num_keys)
    most_common_keys = [key for key,val in most_common_dict]

    pass_nwbinspector = sorted([i for i in nwb_pd['identifier'].loc[(nwb_pd['validation_summary']=='BEST_PRACTICE_VIOLATION')
                                                               | (nwb_pd['validation_summary']=='PASSED_VALIDATION')]])

    readme = '# Summary statistics for available Dandisets\nLast updated: ' + str(date_time) + '\n'
    readme += '\n'
    if bids_exist == 1:
        bids_pd = dandi_metadata_readme.loc[dandi_metadata_readme['data_type'] == bids_type_id].copy()
        bids_pd.reset_index(inplace=True)
        readme += '## BIDS Dandisets\n'
        readme += '\n'
        readme += '- Total number of BIDS Dandisets: ' + str(data_type_dict[bids_type_id]) + '\n'
        readme += '\n'
        readme += '- Median number of files in each BIDS Dandiset: ' + str(
            dandi_metadata_readme['num_files'].loc[dandi_metadata_readme.data_type == bids_type_id].median()) + '\n'
        readme += '\n'
        readme += '- Median number of bytes in each BIDS Dandiset: ' + "{:,}".format(int(
            dandi_metadata_readme['num_bytes'].loc[dandi_metadata_readme.data_type == bids_type_id].median())) + '\n'
    readme += '\n\n'
    readme += '## NWB Dandisets\n'
    readme += '\n'
    readme += '- Total number of NWB Dandisets: ' + str(data_type_dict[nwb_type_id]) + '\n'
    readme += '\n'
    readme += '- Median number of files in each NWB Dandiset: ' + str(
        dandi_metadata_readme['num_files'].loc[dandi_metadata_readme.data_type == nwb_type_id].median()) + '\n'
    readme += '\n'
    readme += '- Median number of bytes in each NWB Dandiset: ' + "{:,}".format(int(
        dandi_metadata_readme['num_bytes'].loc[dandi_metadata_readme.data_type == nwb_type_id].median())) + '\n'
    readme += '\n'
    readme += '- ' + str(num_keys) + ' most commonly measured variables: ' + ', '.join(['%s' % var for var in most_common_keys]) + '\n'
    readme += '\n'
    readme += '- NWB Dandisets that pass NWBInspector and thus are possibly NWBE compatible: '
    root_url = 'https://dandiarchive.org/Dandiset/'
    readme = readme[:-2]+'\n\n'
    for ds in pass_nwbinspector:
        readme += '[%s](#%s), '%(ds, ds)
    readme = readme[:-2]+'\n\n'

    readme += '- NWBE compatibility terminology: \n'
    readme += '  - **LL-P**: Likely plottable - file whose datatypes extend TimeSeries that can be viewed and plotted \n'
    readme += '  - **LL-V**: Likely viewable - file whose datatypes might not extend TimeSeries that can be viewed \n'
    readme += '  - **NC-0**: Not compatible level 0 - file cannot be opened \n'
    readme += '  - **NC-1**: Not compatible level 1 - geppetto model for file cannot be created \n'
    readme += '  - **NI**: No information - file is not tested \n\n'
    readme += '<details open><summary> Summary information on the available Dandisets (full details in <a href="dandiset_summary.csv">dandiset_summary.csv</a>).\n</summary><p>'
    readme += '\n\n\n\n'
    readme += '---\n'

    for row in dandi_metadata_readme.index:
        ref = dandi_metadata_readme['identifier'].iloc[row]
        validation_file = ref + '_validation'

        idn = dandi_metadata_readme['identifier'].iloc[row]
        readme += '<a id="'+idn+'">' + '*[DANDI:' + idn + ']' + '(' + dandi_metadata_readme['url'].iloc[
            row] + ')*' + ': **' + dandi_metadata_readme['name'].iloc[row] + '**</a>\n\n'


        if not pd.isna(dandi_metadata_readme['data_type'].iloc[row]):
            readme += '- Data type: **' + dandi_metadata_readme['data_type'].iloc[row] + '**'

        if not pd.isna(dandi_metadata_readme['nwb_version'].iloc[row]):
            readme += ' (**version ' + dandi_metadata_readme['nwb_version'].iloc[row]+'**)'

        if not pd.isna(dandi_metadata_readme['num_bytes'].iloc[row]):
            readme += ', file count: **'+str(dandi_metadata_readme['num_files'].iloc[row])+'**, total size (MB): **' + "{:,}".format(round(int(dandi_metadata_readme['num_bytes'].iloc[row])/1000000,2)) + '**\n\n'

        if not pd.isna(dandi_metadata_readme['species'].iloc[row]):
            readme += '- Species: **' + dandi_metadata_readme['species'].iloc[row] + '**\n\n'

        if not pd.isna(dandi_metadata_readme['keywords'].iloc[row]):
            kws = ast.literal_eval(dandi_metadata_readme['keywords'].iloc[row])
            if len(kws)>0:
                readme += '- Keywords: ' + ', '.join(['**%s**'%kw for kw in kws]) + '\n\n'

        if not pd.isna(dandi_metadata_readme['variableMeasured'].iloc[row]):
            vars = ast.literal_eval(dandi_metadata_readme['variableMeasured'].iloc[row])
            readme += '- Variables measured: ' + ', '.join(['**%s**'%var for var in vars])  + '\n\n'

        if not pd.isna(dandi_metadata_readme['citation'].iloc[row]):
            readme += '- Source paper: *' + dandi_metadata_readme['citation'].iloc[row].split('(Vers')[0].strip() + '*\n\n'

        if pd.isna(dandi_metadata_readme['validation_summary'].iloc[row]):
            pass
        else:
            if dandi_metadata_readme['validation_summary'].iloc[row] not in ['NULL_FILE_LIMIT', 'UNABLE', 'NOT_DOWNLOADED']:
                val_str = dandi_metadata_readme['validation_summary'].iloc[row].replace(',',', ')
                status = STATUS_AMBER
                if 'PASSED_VALIDATION' in val_str:
                    status = STATUS_GREEN
                readme += '- '+status+' Validation results summary: [' + val_str + ']' + '(%s.txt) \n\n' % (validation_file)

                for i in range(2):
                    compat = dandi_metadata_readme['nwbe_compatibility_' + str(i)].iloc[row]
                    if not pd.isna(compat):
                            
                        readme += '- '
                        if 'LL-P' in compat: readme += STATUS_GREEN
                        elif 'LL-V' in compat: readme += STATUS_AMBER
                        else: readme += STATUS_RED
                        readme += ' NWBE compatibility - example file '+str(i + 1) +': **' + compat + '**  \n'
                    if not pd.isna(dandi_metadata_readme['file_' + str(i)].iloc[row]):
                        nwbe_link = 'http://nwbexplorer.opensourcebrain.org/nwbfile=' + dandi_metadata_readme['file_' + str(i)].iloc[
                            row]
                        if not pd.isna(dandi_metadata_readme['parent_folder_' + str(i)].iloc[row]):
                            dandi_link = dandi_metadata_readme['url'].iloc[row] + '/files?location=' + dandi_metadata_readme['parent_folder_' + str(i)].iloc[row] +'%2F'
                        else:
                            dandi_link = dandi_metadata_readme['url'].iloc[row] + '/files?location='
                        
                        info_link = dandi_metadata_readme['file_' + str(i)].iloc[row].split('/download')[0]
                        file_size = dandi_metadata_readme['file_size_' + str(i)].iloc[row]
                        readme += '   Size: %s MB | \n' % (str(round(int(file_size)/1000000,2)))
                        readme += '[File info](%s) | \n' % (info_link)
                        readme += '[View on DANDI Web](%s) | \n' % (dandi_link)
                        readme += '[View on NWB Explorer](%s) ' % (nwbe_link)
                        if os.path.exists(os.path.join(os.path.join(summary_folder,ref),'file_'+str(i)+'/README.md')):
                            readme += '| \n[File Summary](%s) \n' % (os.path.join(os.path.join('Summaries',ref),'file_'+str(i)+'/README.md'))
                        else:
                            readme +='\n'

            else:
                readme += '- '+STATUS_RED+' Validation results summary: ' + dandi_metadata_readme['validation_summary'].iloc[row] + '\n\n'

        readme += '---'
        readme += '\n\n'
    readme += '</p></details>'
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
                        help='only process first 10 Dandisets if so chosen')
    parser.add_argument('--update_readme_option', default=False, action='store_true',
                        help='update readme file after summary file is created')
    parser.add_argument('--update_readme_only', default=False, action='store_true',
                        help='update readme file without creating summary file')
    parser.add_argument('--test_docker', default=False, action='store_true',
                        help='test using the NWBE docker container')
    parser.add_argument('--create_summary', default=False, action='store_true',
                        help='Create summaries for files which do not contain a summary README.md')
    args = parser.parse_args()
    update_readme_option=create_dandiset_summary(args.no_download,args.no_sizelimit,args.dandiset_limit,
                                                 args.update_readme_option,args.update_readme_only,args.test_docker,args.create_summary)

    if update_readme_option:
        update_readme(args.test_docker)

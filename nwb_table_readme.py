import os
import pandas as pd
import yaml
import math
import json
from datetime import date
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import save_report, format_messages, MessageFormatter


def create_dandiset_summary(hard_limit = 1000000000):

    from dandi.pynwb_utils import get_nwb_version
    import datalad.api as dl
    from dandi import download


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

    dandiset_folder_name = sorted([item for item in os.listdir(root_folder) if item.startswith('0')])
    yaml_file = 'dandiset.yaml'

    yaml_df_flatten = ['identifier','citation','name','assetsSummary.numberOfBytes','assetsSummary.numberOfFiles',
                       'assetsSummary.numberOfSubjects','assetsSummary.variableMeasured','keywords','schemaKey','schemaVersion','url','version']
    tmp_col = ['species','data_type','doi_link','nwb_version','validation_summary','max_file_size','min_file_size']
    readme_table = ['identifier','data_type','num_files','num_bytes','dandiset_schemaver','url', 'nwb_version','validation_summary','max_file_size','min_file_size']

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
        largest_file_size = nanval
        smallest_size_lst = [nanval,nanval]
        validation_summary = nanval
        if data_type != nanval and 'NWB' in str(data_type):
            # get the json file that has individual files info
            with open(os.path.join(root_folder, dandiset_name, json_file)) as f:
                data = json.load(f)
            # flatten json file to pandas table
            json_df = pd.json_normalize(data)
            # sort the dataframe by column size will prevent returning series of files that have the same size
            json_df.sort_values(by='size', inplace=True)
            # get the file path with the smallest size first, and check if it is a valid nwb file in the while loop
            path_file = json_df['path'].iloc[0]
            path_lst = []
            url_lst = []
            smallest_size_lst = []
            counter = 0
            valid_path_url = 0
            # a dataset might only have 1 file, and max_counter is the number of valid nwb files we want
            max_counter = 2
            if len(json_df) == 1:
                max_counter = 1
            while valid_path_url < max_counter:
                # check if the file with smallest file size is nwb, if not, get the next row
                if path_file.split('.')[-1] != 'nwb':
                    counter += 1
                    path_file = json_df['path'].iloc[counter]
                # if it is, return the path
                else:
                    valid_path_url += 1
                    path_lst.append(path_file)
                    dandi_url = json_df['metadata.contentUrl'].iloc[counter][0]
                    url_lst.append(dandi_url)
                    smallest_size_lst.append(json_df['size'].iloc[counter])
                    # reinsatntiate path_file so it passes the first if
                    path_file = 't.blah'
                # in case the while loop loops through all the length of the dataframe
                if counter == len(json_df)-1:
                    break
            largest_file_size = json_df['size'].iloc[-1]
            report_message = []
            # in case files larger than the hard_limit
            validation_summary = 'NULL_FILE_LIMIT'
            # only download files that has size lower than the hard limit
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
                    # uninstall file
                    os.unlink(nwb_path)
        # concatenate the additional variables to the flattened pdf
        yaml_df = pd.concat([yaml_df, pd.DataFrame([[species_name,data_type,doi_link,nwb_version,validation_summary,largest_file_size,smallest_size_lst[0]]],
                                                   index=yaml_df.index,columns=tmp_col)],axis=1)

        # concatenate every newly read dandiset metadata dataframe
        dandi_metadata = pd.concat([dandi_metadata,yaml_df],axis=0,ignore_index=True)
        dandi_metadata.to_csv('dandiset_summary_tmp.csv')
        f.close()

    # only get the relevant columns
    yaml_df_flatten.extend(tmp_col)
    dandi_metadata_final = dandi_metadata[yaml_df_flatten].sort_values(by=['identifier'],ignore_index=True)
    dandi_metadata_final.rename(columns={'assetsSummary.numberOfBytes':'num_bytes','assetsSummary.numberOfFiles':'num_files','assetsSummary.numberOfSubjects':'numb_subjects',
                                         'assetsSummary.variableMeasured':'variableMeasured', 'schemaVersion':'dandiset_schemaver'},inplace=True)
    # get table for readme
    dandi_metadata_readme = dandi_metadata_final[readme_table]
    # save table to csv
    dandi_metadata_final.to_csv('dandiset_summary.csv')
    dandi_metadata_readme.to_csv('dandiset_summary_readme.csv')

    # # remove the cloned dandisets folder
    dl.remove(dataset=root_folder)

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
    rd_file = 'README.md'
    if not os.path.exists('dandiset_summary.csv'):
        exit()
    # Getting Datetime from timestamp
    date_time = date.today()
    dandi_metadata_readme = pd.read_csv('dandiset_summary.csv')
    dandi_metadata_readme.drop(dandi_metadata_readme.filter(regex="Unnamed"), axis=1, inplace=True)
    dandi_metadata_readme.to_csv('dandiset_summary.csv', index=False)
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
    nwbe_compatible = sorted([i+',' for i in nwb_pd['identifier'].loc[(nwb_pd['validation_summary']=='BEST_PRACTICE_VIOLATION')
                                                               | (nwb_pd['validation_summary']=='PASSED_VALIDATION')]])
    nwb_pd['validation_summary'].fillna('NULL_FILE_LIMIT', inplace=True)

    readme = '# DANDI Archive Showcase\n'
    readme += '\n'
    readme += 'Scripts for interacting with the [DANDI Archive](https://www.dandiarchive.org/), particularly from [OSBv2](https://docs.opensourcebrain.org/OSBv2/Overview.html).\n'
    readme += '\n'
    readme += '## Summary statistics for the available NWB dandisets (Updated on ' + str(date_time) + ')' '\n'
    readme += '\n'
    readme += '- Total number of NWB dandisets: ' + str(data_type_dict[nwb_type_id]) + '\n'
    readme += '\n'
    readme += '- Median number of files in each NWB dandiset: ' + str(
        dandi_metadata_readme['num_files'].loc[dandi_metadata_readme.data_type == nwb_type_id].median()) + '\n'
    readme += '\n'
    readme += '- Median number of bytes in each NWB dandiset: ' + str(
        dandi_metadata_readme['num_bytes'].loc[dandi_metadata_readme.data_type == nwb_type_id].median()) + '\n'
    readme += '\n'
    readme += '- NWB dandiset that are possibly NWBE compatible: ' + ' '.join(nwbe_compatible)[:-2] + '\n'
    readme += '\n'
    readme += '<details><summary> Summary information on the available NWB dandisets (more details in dandiset_summary.csv).\n</summary><p>'
    readme += '\n\n\n\n'

    for row in nwb_pd.index:
        ref = nwb_pd['identifier'].iloc[row]
        validation_file = 'validation_folder/' + ref + '_validation'
        try:
            readme += '*[DANDI:' + nwb_pd['identifier'].iloc[row] + ']' + '(' + nwb_pd['url'].iloc[
                row] + ')*' + ': **' + nwb_pd['name'].iloc[row] + '**\n\n'
        except:
            pass
        if not pd.isna(nwb_pd['nwb_version'].iloc[row]):
            readme += '- NWB version: ' + nwb_pd['nwb_version'].iloc[row] + '\n\n'
        if not pd.isna(nwb_pd['num_bytes'].iloc[row]):
            readme += '- Dandiset size (in bytes): ' + str(nwb_pd['num_bytes'].iloc[row]) + '\n\n'
        if not nwb_pd['validation_summary'].iloc[row] in ['NULL_FILE_LIMIT', 'UNABLE']:
            readme += '- Validation results summary: [' + nwb_pd['validation_summary'].iloc[
                row] + ']' + '(%s.txt) \n\n' % (validation_file)
        else:
            readme += '- Validation results summary: ' + nwb_pd['validation_summary'].iloc[row] + ' \n\n'
        if not pd.isna(nwb_pd['species'].iloc[row]):
            readme += '- Species: ' + nwb_pd['species'].iloc[row] + '\n\n'
        if not pd.isna(nwb_pd['variableMeasured'].iloc[row]):
            readme += '- Variables measured: ' + nwb_pd['variableMeasured'].iloc[row] + '\n\n'
        if not pd.isna(nwb_pd['citation'].iloc[row]):
            readme += '- Source paper: ' + nwb_pd['citation'].iloc[row].split('(Vers')[0] + '\n\n'

        readme += '---'
        readme += '\n\n'
    readme += '</p></details>'
    rmd = open(rd_file, 'w')
    rmd.write(readme)
    rmd.close()

if __name__ == '__main__':
    create_dandiset_summary(hard_limit=10)
    update_readme()

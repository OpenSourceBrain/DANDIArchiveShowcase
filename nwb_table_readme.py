import os
from pathlib import Path
import pandas as pd
import yaml
import math
import datalad.api as dl
from mdtable import MDTable
import json
from datetime import date
from dandi.pynwb_utils import get_nwb_version
from dandi.dandiapi import DandiAPIClient
from hdmf.backends.hdf5 import HDF5IO
from dandi import download

def create_dandiset_summary():
    hard_limit = 1000000000
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

    dandiset_folder_name = [item for item in os.listdir(root_folder) if item.startswith('0')]
    yaml_file = 'dandiset.yaml'

    yaml_df_flatten = ['identifier','citation','name','assetsSummary.numberOfBytes','assetsSummary.numberOfFiles','assetsSummary.numberOfSubjects','assetsSummary.variableMeasured','keywords','schemaKey','schemaVersion','url','version']
    tmp_col = ['species','data_type','doi_link','nwb_version']
    readme_table = ['identifier','data_type','num_files','num_bytes','dandiset_schemaver','url', 'nwb_version','max_file_size','min_file_size']

    dandi_metadata = pd.DataFrame()
    nanval = math.nan
    lst_count =[]
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
            # nwb_version = nanval
        try:
            doi_link = my_dict['relatedResource'][0]['url']
        except:
            doi_link = nanval

        # flatten the yaml file and read in into dataframe
        yaml_df = pd.json_normalize(my_dict)

        # get nwb version for NWB dandisets
        nwb_version = nanval
        largest_file_size = nanval
        smallest_file_size = nanval
        if data_type != nanval and 'NWB' in str(data_type):
            # get the json file that has individual files info
            with open(os.path.join(root_folder, dandiset_name, json_file)) as f:
                data = json.load(f)
            # flatten json file to pandas table
            json_df = pd.json_normalize(data)
            largest_file_size = json_df['size'].max(axis=0)
            smallest_file_size = json_df['size'].min(axis=0)
            json_df.set_index('size', inplace=True)
            # there might be more than one file that has the smallest file size. if so, dandi_url will be return as a series
            dandi_url_gen = json_df.at[smallest_file_size, 'metadata.contentUrl']
            if type(dandi_url_gen) == list:
                dandi_url = dandi_url_gen[0]
                nwb_file_name = json_df.at[smallest_file_size, 'path']
            else:
                dandi_url = dandi_url_gen.iloc[0][0]
                nwb_file_name = json_df.at[smallest_file_size, 'path'].iloc[0]

            # only download files that has size lower than the hard limit
            if smallest_file_size < hard_limit:
                nwb_version = extract_nwb_version(dandi_url,nwb_file_name,nwb_version)

            print(data_type)
            print(nwb_version)
        # concatenate the additional variables to the flattened pdf
        yaml_df = pd.concat([yaml_df, pd.DataFrame([[species_name,data_type,doi_link,nwb_version,largest_file_size,smallest_file_size]],index=yaml_df.index,columns=tmp_col)],axis=1)

        # concatenate every newly read dandiset metadata dataframe
        dandi_metadata = pd.concat([dandi_metadata,yaml_df],axis=0,ignore_index=True)
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
    # dl.remove(dataset=root_folder)

def extract_nwb_version(dandi_url,nwb_file_name,nwb_version=None):
    # the argument nwb_version is in case the function exits with error
    # create save folder
    save_folder = '/tmp/nwb_versions'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    # # tracker to only get
    # count = 0
    # if dandi_url == None:
    #     with DandiAPIClient() as client:
    #         dandiset = client.get_dandiset(dds_id, dds_version)
    #         for asset in dandiset.get_assets():
    #             dandi_url = asset.get_raw_metadata().get('contentUrl')[0]
    #             nwb_file_name = asset.get_raw_metadata().get('path')
    #             count +=1
    #             if count == 1:
    #                 break

    # assumes that nwb_file_name follows the format subdataset_name/file_name
    if '/' in nwb_file_name:
        tmp_nwb_path = os.path.join(save_folder, nwb_file_name.split('/')[-1])
    else:
        tmp_nwb_path = os.path.join(save_folder, nwb_file_name)
    # download 1 file here
    download.download(dandi_url, output_dir=save_folder)
    # get nwb_schema version
    nwb_version = get_nwb_version(tmp_nwb_path)
    os.unlink(tmp_nwb_path)
    # except:
    #     print('error somewhere ' + nwb_file_name)

    # if dandi_url != None:
    #     # download 1 file here
    #     download.download(dandi_url, output_dir=save_folder)
    #     # get nwb_schema version
    #     nwb_version = get_nwb_version(tmp_nwb_path)
    #     # uninstall file
    #     try:
    #         os.unlink(tmp_nwb_path)
    #     except OSError:
    #         print('OSError from os.unlink for file ' + nwb_file_name)
    # else:
    #     dl.get(path=os.path.join(dataset_path, nwb_file_name))
    #     # get nwb_schema version
    #     nwb_version = get_nwb_version(path=os.path.join(dataset_path, nwb_file_name))
    #     # print(a)
    #     # namespaces = HDF5IO.get_namespaces(path=os.path.join(dataset_path, nwb_file_name))
    #     # nwb_version = namespaces['core']
    #     # uninstall file
    #     try:
    #         dl.drop(os.path.join(dataset_path, nwb_file_name))
    #     except:
    #         print('datalad is crazy')
    return nwb_version

def update_readme():
    if not os.path.exists('dandiset_summary_readme.csv'):
        exit()
    # Getting Datetime from timestamp
    date_time = date.today()
    dandi_metadata_readme = pd.read_csv('dandiset_summary_readme.csv')
    dandi_metadata_readme.drop(dandi_metadata_readme.filter(regex="Unnamed"), axis=1, inplace=True)
    dandi_metadata_readme.to_csv('dandiset_summary_readme.csv',index=False)
    print(dandi_metadata_readme)
    # summary statistics here
    data_type_dict = dandi_metadata_readme['data_type'].value_counts().to_dict()
    # get data_type values
    for k,vals in data_type_dict.items():
        if 'NWB' in k:
            nwb_type_id = k

    markdown = MDTable('dandiset_summary_readme.csv')
    markdown_string_table = markdown.get_table()

    readme = '# DANDI Archive Showcase\n'
    readme +='\n'
    readme +='Scripts for interacting with the [DANDI Archive](https://www.dandiarchive.org/), particularly from [OSBv2](https://docs.opensourcebrain.org/OSBv2/Overview.html).\n'
    readme +='\n'
    readme +='Summary statistics for the available NWB dandisets (Updated on ' + str(date_time) +')' '\n'
    readme +='\n'
    readme +='- Total number of NWB dandisets: ' + str(data_type_dict[nwb_type_id]) + '\n'
    readme +='\n'
    readme +='- Median number of files in each NWB dandiset: ' + str(dandi_metadata_readme['num_files'].loc[dandi_metadata_readme.data_type==nwb_type_id].median()) + '\n'
    readme +='\n'
    readme +='- Median number of bytes in each NWB dandiset: ' + str(dandi_metadata_readme['num_bytes'].loc[dandi_metadata_readme.data_type==nwb_type_id].median()) + '\n'
    readme +='\n'
    readme +='Summary table for the available dandisets (more details in dandiset_summary.csv).\n'
    readme +='\n\n'
    rmd = open('README.md', 'w')
    rmd.write(readme)
    rmd.write(markdown_string_table)
    rmd.close()

if __name__ == '__main__':
    create_dandiset_summary()
    # update_readme()



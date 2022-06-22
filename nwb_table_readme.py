import os
import pandas as pd
import yaml
import math
import datalad.api as dl
from mdtable import MDTable

# clone the dandisets - powered by Datalad - repo
dl.install(source='https://github.com/dandi/dandisets.git',recursive=True)
# root folder where dandisets repo is cloned
root_folder ='dandisets'
dandiset_folder_name = [item for item in os.listdir(root_folder) if item.startswith('0')]
yaml_file = 'dandiset.yaml'

yaml_df_flatten = ['identifier','citation','name','assetsSummary.numberOfBytes','assetsSummary.numberOfFiles','assetsSummary.numberOfSubjects','assetsSummary.variableMeasured','keywords','schemaKey','schemaVersion','url','version']
tmp_col = ['species','data_type','doi_link']
readme_table = ['identifier','data_type','num_files','num_bytes','dandiset_schemaver','url']

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
    # concatenate the additional variables to the flattened pdf
    yaml_df = pd.concat([yaml_df, pd.DataFrame([[species_name,data_type,doi_link]],index=yaml_df.index,columns=tmp_col)],axis=1 )

    # concatenate every newly read dandiset metadata dataframe
    dandi_metadata = pd.concat([dandi_metadata,yaml_df],axis=0,ignore_index=True)
    f.close()

# only get the relevant columns
yaml_df_flatten.extend(tmp_col)
dandi_metadata_final = dandi_metadata[yaml_df_flatten]
dandi_metadata_final.rename(columns={'assetsSummary.numberOfBytes':'num_bytes','assetsSummary.numberOfFiles':'num_files','assetsSummary.numberOfSubjects':'numb_subjects',
                                     'assetsSummary.variableMeasured':'variableMeasured', 'schemaVersion':'dandiset_schemaver'},inplace=True)
# remove faux dandisets
# dandi_metadata_final.drop(dandi_metadata_final[dandi_metadata_final['num_bytes'] == 0].index, inplace=True)
# get table for readme
dandi_metadata_readme = dandi_metadata_final[readme_table]
# save table to csv
dandi_metadata_final.to_csv('../dandiset_summary.csv')
dandi_metadata_readme.to_csv('../dandiset_summary_readme.csv')

markdown = MDTable('../dandiset_summary_readme.csv')
markdown_string_table = markdown.get_table()

readme = '# DANDI Archive Showcase\n'
readme +='\n'
readme +='Scripts for interacting with the [DANDI Archive](https://www.dandiarchive.org/), particularly from [OSBv2](https://docs.opensourcebrain.org/OSBv2/Overview.html).\n'
readme +='\n'
readme +='Summary table for the available dandisets (more details in dandiset_summary.csv).\n'
readme +='\n\n'
rmd = open('../README.md', 'w')
rmd.write(readme)
rmd.write(markdown_string_table)
rmd.close()


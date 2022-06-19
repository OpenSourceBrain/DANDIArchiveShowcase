import os
import pandas as pd
import yaml
import math
from mdtable import MDTable

root_folder ='/home/anh/Documents/gsoc/nwb_project/dandisets'
dandiset_folder_name = [item for item in os.listdir(root_folder) if item.startswith('0')]
yaml_file = 'dandiset.yaml'

yaml_df_flatten = ['identifier','citation','name','assetsSummary.numberOfBytes','assetsSummary.numberOfFiles','assetsSummary.numberOfSubjects','assetsSummary.variableMeasured','keywords','schemaKey','schemaVersion','url','version']
tmp_col = ['species','data_type','doi_link']

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
dandi_metadata_final.rename(columns={'assetsSummary.numberOfBytes':'numberOfBytes','assetsSummary.numberOfFiles':'numberOfFiles','assetsSummary.numberOfSubjects':'numberOfSubjects','assetsSummary.variableMeasured':'variableMeasured'},inplace=True)
# save table to csv
dandi_metadata_final.to_csv('dandiset_summary.csv')

markdown = MDTable('dandiset_summary.csv')
markdown_string_table = markdown.get_table()

readme = '# DANDI Archive Showcase\n'
readme +='\n'
readme +='Scripts for interacting with the [DANDI Archive](https://www.dandiarchive.org/), particularly from [OSBv2](https://docs.opensourcebrain.org/OSBv2/Overview.html).\n'
readme +='\n\n'
rmd = open('../README.md', 'w')
rmd.write(readme)
rmd.write(markdown_string_table)
rmd.close()


'''
A script to get dandiset/individual nwb files based on user input. In development.
'''
import datalad.api as dl
import sys
import pandas as pd
import json
import os

# TODO: add test.py and test_compatibility.py

def get_nwb(dandiset_id):
    dataset_path = input('Target directory (has to be an empty folder) ')
    github_link_format = 'https://github.com/dandisets/'
    json_file = '.dandi/assets.json'

    dl.install(path=dataset_path,source=github_link_format+dandiset_id,recursive=True)

    # import json
    with open(os.path.join(dataset_path,json_file)) as f:
      data = json.load(f)
    # flatten json file to pandas table
    json_df = pd.json_normalize(data)
    # only get individual file's path and size
    cols = ['path','size']
    json_df = json_df[cols]

    # print table here with total bytes info
    print('Files in dandiset and their sizes')
    pd.set_option('display.max_colwidth',1000)
    pd.set_option('display.max_rows',1000)
    print(json_df)

    # ask if user wants to download entire dataset or selective files
    total_bytes = json_df['size'].sum()
    ans = input('The dandiset is ' + str(total_bytes) + ' bytes big. Do you want to download the dandiset or some of its files? (0:dandiset | 1: some files) ')

    if ans == '0':
        dl.get(dataset_path, recursive=True, get_data=True)
    else:
        num_file = input('Number of files to download: ')
        if num_file == '0':
            print('No files wanted. Exiting...')
            exit()
        else:
            file_path = input('Please specify the file path(s) as shown in the table. If multiple files, please separate them by commas. ')
            try:
                nwb_file_list = list(file_path.split(','))
                # to get rid of possible white spaces
                for i in range(len(nwb_file_list)):
                    nwb_file_list[i] = nwb_file_list[i].strip()
            except:
                nwb_file_list = list(file_path.strip())

            for nwb_file in nwb_file_list:
                dl.get(os.path.join(dataset_path,nwb_file))

# validate pynwb
# test.py nwb_filename

# test compatibility
# test_compatibility nwb_filename

if __name__ == "__main__":
    if len(sys.argv)==1:
        print('Please specify the dandiset you want (example input: 000xxx)')
        exit()

    get_nwb(str(sys.argv[1]))
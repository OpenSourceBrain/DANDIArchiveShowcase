'''
A script to get dandiset/individual nwb files based on user input. In development.
'''
import datalad.api as dl
import sys
import pandas as pd
import json
import os
from pynwb import validate, NWBHDF5IO

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
    ans = input('The dandiset is ' + str(total_bytes) + ' bytes big. '
                'Do you want to download the dandiset or some of its files? (0:dandiset | 1: some files) ')

    if ans == '0':
        dl.get(dataset_path, recursive=True, get_data=True)
        return dandiset_id, dataset_path
    else:
        num_file = input('Number of files to download: ')
        if num_file == '0':
            print('No files wanted. Exiting...')
            exit()
        else:
            file_path = input('Please specify the file path(s) as shown in the table. '
                              'If multiple files, please separate them by commas. ')
            try:
                nwb_file_list = list(file_path.split(','))
                # to get rid of possible white spaces
                for i in range(len(nwb_file_list)):
                    nwb_file_list[i] = nwb_file_list[i].strip()
            except:
                nwb_file_list = list(file_path.strip())

            for nwb_file in nwb_file_list:
                dl.get(os.path.join(dataset_path,nwb_file))

    return nwb_file_list, dataset_path

def validate_nwb_file(nwb_file_list, dataset_path):
    # TODO: save error and file name to a csv file outside of dataset_path (datalad status conflict)

    print('Starting to validate NWB files...')
    save_dir = input(
        'Please specify a directory outside the folder of the installed dandiset/files '
        'where the validation report can be saved: ')

    # in the case of a whole dandiset being installed, dandi_set_id is returned as nwb_file_list
    if isinstance(nwb_file_list, basestring):
        ans = input('It seems you installed the whole dandiset. '
                    'Do you want to validate all files or just some files, or none at all? '
                    '(0-all | 1-some | 2-none')
        if ans == '0':
            # os.walk to get all the nwb files, nwb_file_list now contains the full path to files
            nwb_file_list = []
            for dirpath, subdirs, files in os.walk(dataset_path):
                nwb_file_list.extend(os.path.join(dirpath, x) for x in files if x.endswith(".nwb"))
        elif ans == '1':
            nwb_to_validate = input('Please specify the file path(s) as shown in the table. '
                                    'If multiple files, please separate them by commas. ')
            try:
                nwb_file_list = list(nwb_to_validate.split(','))
                # to get rid of possible white spaces
                for i in range(len(nwb_file_list)):
                    nwb_file_list[i] = nwb_file_list[i].strip()
            except:
                nwb_file_list = list(nwb_to_validate.strip())
        else:
            print('Nothing to validate. Exiting...')
            exit()
    else:
        # an arbitrary flag for nwb_file_list not containing the full file path for each file
        ans = '3'

    if ans != '0':
        for nwb_file in nwb_file_list:
            os.system('python -m pynwb.validate '+ os.path.join(dataset_path,nwb_file))
            # update table report
    else:
        for nwb_file in nwb_file_list:
            os.system('python -m pynwb.validate '+ nwb_file)
            # update table report
    # save table report
    print('Validation finished. Report is saved as test_summary.csv at '+ save_dir)

# test compatibility
# test_compatibility nwb_filename

if __name__ == "__main__":
    if len(sys.argv)==1:
        print('Please specify the dandiset you want (example input: 000xxx)')
        exit()

    nwb_file_list, dataset_path = get_nwb(str(sys.argv[1]))

    # start validate nwb files here
    validate_nwb_file(nwb_file_list, dataset_path)




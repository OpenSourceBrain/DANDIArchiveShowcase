'''
A script to get dandiset/individual nwb files based on user input. In development.
'''
import datalad.api as dl
import sys
import pandas as pd
import json
import os
from nwbinspector import inspect_nwb, inspect_all
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import format_messages, save_report

# TODO: add test_compatibility.py

def get_nwb(dandiset_id):
    dataset_path = input('Target directory (if dandiset not already exists, this has to be an empty folder) ')
    github_link_format = 'https://github.com/dandisets/'
    json_file = '.dandi/assets.json'

    # only clone dandiset if directory is empty
    dir = os.listdir(dataset_path)
    if len(dir) == 0:
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
        # params dataset is for instances where current working directory does not contain the cloned datasets
        dl.get(dataset_path, recursive=True, get_data=True,dataset=dataset_path)
        nwb_file_list = dandiset_id
    elif ans == '1':
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
            dl.get(os.path.join(dataset_path,nwb_file),dataset=dataset_path)
    else:
        exit()
    return nwb_file_list, dataset_path

def validate_nwb_file(dandiset_id,nwb_file_list, dataset_path):
    validate_decision = input('Do you want to validate these files? (0-no | 1-yes) ')
    if validate_decision == '0':
        exit()

    save_dir = input(
        'Please specify a directory outside the folder of the installed dandiset/files '
        'where the validation report can be saved: ')

    # placeholder for case where whole dandiset is not installed
    ans = 2
    if isinstance(nwb_file_list, str):
        ans = input('It seems you installed the whole dandiset. '
                    'Do you want to validate all files or just some files (0-all | 1-some)? ')
        if ans == '1':
            nwb_to_validate = input('Please specify the file path(s) as shown in the table. '
                                    'If multiple files, please separate them by commas. ')
            try:
                nwb_file_list = list(nwb_to_validate.split(','))
                # to get rid of possible white spaces
                for i in range(len(nwb_file_list)):
                    nwb_file_list[i] = nwb_file_list[i].strip()
            except:
                nwb_file_list = list(nwb_to_validate.strip())

    # in the case of whole dandiset, nwb_file_list is the dandiset_id
    if ans == '0':
        report_name = 'report_' + dandiset_id
        report_message = list(inspect_all(path=dataset_path, progress_bar=True,
                                          importance_threshold=Importance.BEST_PRACTICE_VIOLATION))
    else:
        # initialize nwb inspector report
        report_name = 'report_' + dandiset_id + '_files'
        report_message = []
        for nwb_file in nwb_file_list:
            nwb_file_path = os.path.join(dataset_path, nwb_file)
            report_message.extend(list(inspect_nwb(nwbfile_path=nwb_file_path,
                                                   importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))
    # save table report
    report_path = os.path.join(save_dir,report_name+'.csv')
    if os.path.isfile(report_path):
        report_name = report_name +'_'
        print('File already exists. Saving file with a new name.')
    save_report(report_file_path=os.path.join(save_dir,report_name+'.txt'),
                formatted_messages=format_messages(report_message, levels=['importance', 'location']), overwrite=True)
    print('Validation finished. Report is saved as ' +report_name+'.txt' + ' at '+ save_dir)

# test compatibility
# test_compatibility nwb_filename

if __name__ == "__main__":
    if len(sys.argv)==1:
        print('Please specify the dandiset you want (example input: 000xxx)')
        exit()
    nwb_file_list, dataset_path = get_nwb(str(sys.argv[1]))
    # start validate nwb files here
    validate_nwb_file(str(sys.argv[1]), nwb_file_list, dataset_path)
import pandas as pd
import os
import argparse
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
from datetime import date
import subprocess
from pathlib import Path
from nwb_table_readme import nwb_inspector_message_format

def validate_nwb(arge_github_link=None,arge_parse_message=None):

    # decide message detail levels - since we're streaming files, file names are urls
    if arge_parse_message:
        message_levels = ['importance', 'file_path']
    else:
        message_levels = ['importance', 'location']
    if arge_github_link:
        # clone the repo into a target folder
        target_folder ='blah'
        output = subprocess.check_output(["git", "clone", "https://github.com/OpenSourceBrain/NWBShowcase.git","targetfolder"])
        # get the nwb file paths
        nwbfiles=list(Path(target_folder).rglob('*.nwb'))
        # turn the list to dataframe for easy handle and preserving file order
        df = pd.DataFrame(nwbfiles,columns=['nwbfile_path'])
        df['parent_folder'] = df['nwbfile_path'].apply(lambda row : row.parent.name)
        # turn the dataframe to dict with keys as parent folder and values as corresponding nwbfile paths
        nwbfile_dict = df.groupby('parent_folder')['nwbfile_path'].apply(list)
        # start inspecting nwb files grouped by parent folder
        for parent_folder, nwbfile_path in nwbfile_dict.items():
            print(parent_folder)
            report_message=[]
            for i in range(len(nwbfile_path)):
                report_message.extend(list(inspect_nwb(nwbfile_path=nwbfile_path[i],
                                                       importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))

            validation_summary = nwb_inspector_message_format(report_message, parent_folder)
        # remove the cloned repo once done
        os.unlink(target_folder)
    # if not a github repo, input is list of local nwb file path
    else:
        file_path = input('Please give the paths of files you want to inspect. '
                          'If multiple files, please separate them by commas. ')
        try:
            nwbfile_path = list(file_path.split(','))
            # to get rid of possible white spaces
            for i in range(len(nwbfile_path)):
                nwbfile_path[i] = nwbfile_path[i].strip()
        except:
            nwbfile_path = list(file_path.strip())

        parent_folder = 'NWB'
        report_message = []
        for i in range(len(nwbfile_path)):
            report_message.extend(list(inspect_nwb(nwbfile_path=nwbfile_path[i],
                                                   importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))

        validation_summary = nwb_inspector_message_format(report_message, parent_folder)


if __name__ == "__main__":
    # option for testing and option for bulk
    parser = argparse.ArgumentParser(description='bulk validating nwb dandisets')
    parser.add_argument('--github_link', default=False, action='store_true', help='only test 2 files in 5 dandisets')
    parser.add_argument('--succint', default=False, action='store_true',
                        help='return detailed report messages')
    args = parser.parse_args()
    validate_nwb(args.github_link, args.succint)

    # if len(sys.argv)==1:
    #     print('Please specify the dandiset you want (example input: 000xxx)')
    #     exit()
    # nwb_file_list, dataset_path = get_nwb(str(sys.argv[1]))
    # # start validate nwb files here
    # validate_nwb_file(str(sys.argv[1]), nwb_file_list, dataset_path)

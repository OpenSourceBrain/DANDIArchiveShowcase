import pandas as pd
import os
import argparse
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
import subprocess
from pathlib import Path
from nwb_table_readme import nwb_inspector_message_format

def inspect_nwb_bulk(arge_folder_path=None):
    # where the reports will be saved to
    report_save_folder = 'validation_folder/nwbinspector_bulk'
    # if not a github repo, input is list of local nwb file path
    if arge_folder_path:
        target_folder = input('Please specify the directory that has the NWB files you want to inspect: ')
    else:
        # clone the repo into a target folder
        target_folder = '/tmp/github'
        os.mkdir(target_folder)
        subprocess.run(
            ["git", "clone", "https://github.com/OpenSourceBrain/NWBShowcase.git", target_folder])
    # get the nwb file paths
    nwbfiles=list(Path(target_folder).rglob('*.nwb'))
    # turn the list to dataframe for easy handle and preserving file order
    df = pd.DataFrame(nwbfiles,columns=['nwbfile_path'])
    df['parent_folder'] = df['nwbfile_path'].apply(lambda row : row.parent.name)
    # turn the dataframe to dict with keys as parent folder and values as corresponding nwbfile paths
    nwbfile_dict = df.groupby('parent_folder')['nwbfile_path'].apply(list)
    # start inspecting nwb files grouped by parent folder
    for parent_folder, nwbfile_path in nwbfile_dict.items():
        report_message=[]
        for i in range(len(nwbfile_path)):
            report_message.extend(list(inspect_nwb(nwbfile_path=nwbfile_path[i],
                                                   importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))
        nwb_inspector_message_format(report_message, parent_folder, report_save_folder)

if __name__ == "__main__":
    # option for testing github link or folder path
    parser = argparse.ArgumentParser(description='bulk validating nwb dandisets')
    parser.add_argument('--folder_path', default=False, action='store_true', help='only test 2 files in 5 dandisets')

    args = parser.parse_args()
    inspect_nwb_bulk(args.folder_path)

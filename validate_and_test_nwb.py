'''
A script to validate and test dandiset/individual nwb files' compatibility against NWBE based on user input. In development.
'''
import pandas as pd
import os
import argparse
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import save_report
from nwbinspector.inspector_tools import format_messages
from dandi.dandiapi import DandiAPIClient


# def test_compatibility(nwb_id):

def validate_nwb(arge_parse_bulk=None,arge_parse_message=None):
    # check if dandiset_summary file exists, if not, run nwb_table_readme.py
    if not os.path.exists('dandiset_summary.csv'):
        os.system('python nwb_table_readme.py')
    # read dandiset summary csv file to get dandiset info
    dds_table = pd.read_csv('dandiset_summary.csv',usecols=['identifier','version','data_type'])
    data_type = dds_table.data_type.dropna().unique()
    for i in data_type:
        if 'NWB' in i:
            nwb_type_id = i
    # get the list of nwb dds
    nwb_dds_df = dds_table[['identifier','version']].loc[dds_table.data_type == nwb_type_id]
    # modify the list to get id with 000xxx format
    nwb_dds_df['identifier'] = [i.split(':')[1] for i in nwb_dds_df.identifier]
    # decide message detail levels
    if arge_parse_message:
        message_levels = ['importance', 'file_path']
    else:
        message_levels = ['importance', 'location']

    for dds_index in range(len(nwb_dds_df)):
        # get dds id and version from the table
        dds_id = nwb_dds_df.identifier.iloc[dds_index]
        dds_version = nwb_dds_df.version.iloc[dds_index]
        s3_url = []
        # get s3 url to stream files from
        with DandiAPIClient() as client:
            dandiset = client.get_dandiset(dds_id, dds_version)
            for asset in dandiset.get_assets():
                s3_url.append(asset.get_content_url(follow_redirects=1, strip_query=True))
        # decide the number of files we should test
        if arge_parse_bulk:
            report_name = 'report_' + dds_id + '_files.txt'
            if len(s3_url) < 10:
                num_files = len(s3_url)
            else:
                num_files = round(len(s3_url) * .1)
        else:
            report_name = 'report_' + dds_id + '.txt'
            num_files = len(s3_url)
        # start testing
        report_message = []
        for i in range(num_files):
            report_message.extend(list(inspect_nwb(nwbfile_path=s3_url[i], driver='ros3',
                                                   importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))
        print('Testing is finished for dandiset'+dds_id +'. report is saved as txt file.')
        save_report(report_file_path=report_name,
                    formatted_messages=format_messages(report_message, levels=message_levels),
                    overwrite=True)

if __name__ == "__main__":
    # option for testing and option for bulk
    parser = argparse.ArgumentParser(description='bulk validating nwb dandisets')
    parser.add_argument('--test', default=False, action='store_true', help='only test 10% of the files in each dandiset')
    parser.add_argument('--detailed', default=False, action='store_true',
                        help='return detailed report messages')
    args = parser.parse_args()
    validate_nwb(args.test,args.detailed)

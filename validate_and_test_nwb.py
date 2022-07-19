'''
A script to validate and test dandiset/individual nwb files' compatibility against NWBE based on user input. In development.
'''
import pandas as pd
import os
import argparse
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import save_report, format_messages, MessageFormatter
from dandi.dandiapi import DandiAPIClient
from datetime import date
from nwb_table_readme import update_readme, extract_nwb_version
# def test_compatibility(nwb_id):

def validate_nwb(arge_parse_bulk=None,arge_parse_update=None,arge_parse_message=None):

    # Getting Datetime from timestamp
    date_time = date.today()
    # check if dandiset_summary file exists, if not, run nwb_table_readme.py
    if not os.path.exists('dandiset_summary.csv'):
        os.system('python nwb_table_readme.py')
    # create save folder
    save_folder = '/tmp/validation_dandiset_reports'
    if not os.path.exists(save_folder):
        os.mkdir(save_folder)
    # read dandiset summary csv file to get dandiset info
    dds_table = pd.read_csv('dandiset_summary.csv',usecols=['identifier','version','data_type','num_files'])
    dds_table['validation_result'] = ''
    data_type = dds_table.data_type.dropna().unique()
    for i in data_type:
        if 'NWB' in i:
            nwb_type_id = i

    # get the list of nwb dds - copy() method so that Pandas knows a new df is being operated on
    # if update option is parsed, only test NWB dandisets that don't have the nwb_version info
    if arge_parse_update:
        nwb_dds_df = dds_table.loc[(dds_table['data_type'] == nwb_type_id) & (dds_table['nwb_version'] == NaN)].copy()
    else:
        nwb_dds_df = dds_table.loc[dds_table['data_type'] == nwb_type_id].copy()
    # modify the list to get id with 000xxx format
    dds_id_prefix = nwb_dds_df['identifier'].iloc[0].split(':')[0]
    nwb_dds_df.loc[:,'identifier'] = [i.split(':')[1] for i in nwb_dds_df.loc[:,'identifier']]
    # decide message detail levels - since we're streaming files, file names are urls
    if arge_parse_message:
        message_levels = ['importance', 'file_path']
    else:
        message_levels = ['importance', 'location']

    # decide number of dandisets and files per dandiset for testing
    if arge_parse_bulk:
        # number of dandiset to test
        num_dds = 5
        # number of files per dandiset to test
        nwb_dds_df.loc[:,'num_files'] = 2
        report_suffix = '_test.txt'
    else:
        num_dds = len(nwb_dds_df)
        report_suffix = '.txt'

    # create text file to hold failed reading of nwb files
    if not os.path.exists('failed_nwb_files.txt'):
        f = open('failed_nwb_files.txt', 'w+')
    else:
        f = open('failed_nwb_files.txt', 'a')
        f.write('New session ' + str(date_time))
    f.close()

    for dds_index in range(num_dds):
        # get dds id and version from the table
        dds_id = nwb_dds_df.identifier.iloc[dds_index]
        dds_version = nwb_dds_df.version.iloc[dds_index]
        num_files = nwb_dds_df.num_files.iloc[dds_index]
        report_name = 'report_'+dds_id+report_suffix
        s3_url = []
        nwb_file_name = []
        # flag to exit test loop based on number of files tested
        exit_loop = 0
        # start testing
        report_message = []
        with DandiAPIClient() as client:
            dandiset = client.get_dandiset(dds_id, dds_version)

            for asset in dandiset.get_assets():
                s3_url.append(asset.get_content_url(follow_redirects=1, strip_query=True))
                nwb_file_name.append(asset.get_raw_metadata().get('path'))
                print('Start validating ' + dds_id + ': ' + nwb_file_name[exit_loop])

                try:
                    report_message.extend(list(inspect_nwb(nwbfile_path=s3_url[exit_loop], driver='ros3',
                                                       importance_threshold=Importance.BEST_PRACTICE_VIOLATION)))
                except:
                    f = open('failed_nwb_files.txt', 'a')
                    f.write(dds_id + ': ' + nwb_file_name[exit_loop] + '\n')
                    f.close()
                    continue

                exit_loop += 1
                if exit_loop == num_files:
                    # download 1 file here
                    dandi_url = asset.get_raw_metadata().get('contentUrl')[0]
                    nwb_version = extract_nwb_version(nwb_file_name,dandi_url=dandi_url)
                    break

        print('Testing is finished for dandiset'+dds_id +'. report is saved as txt file.')
        save_report(report_file_path=os.path.join(save_folder,report_name),
                    formatted_messages=format_messages(report_message, levels=message_levels),
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

        # add file names that correspond to urls to report
        nwb_file_info = dict(zip(s3_url,nwb_file_name))
        report_file = open(report_name,'a')
        report_file.write('\n\nFile names that correspond to paths: \n\n')
        for k, v in nwb_file_info.items():
            report_file.write(k + ': ' + v + '\n\n')
        # save summary of validation types at the end of the report file for future retrieval
        report_file.write('\n\nSummary of vaildation types: \n\n')
        report_file.write(validation_summary)
        report_file.close()

        # update validation result column for the dandiset_summary csv files
        dds_id_full = dds_id_prefix+':'+dds_id
        dds_table.loc[dds_table['identifier']==dds_id_full,'validation_result'] = validation_summary
    dds_table_all = pd.read_csv('dandiset_summary.csv')
    dds_table_readme = pd.read_csv('dandiset_summary_readme.csv')
    dds_table_all['validation_result'] = dds_table.loc[:,'validation_result']
    dds_table_readme['validation_result'] = dds_table.loc[:,'validation_result']
    dds_table_all.to_csv('dandiset_summary.csv',index=False)
    dds_table_readme.to_csv('dandiset_summary_readme.csv',index=False)

if __name__ == "__main__":
    # option for testing and option for bulk
    parser = argparse.ArgumentParser(description='bulk validating nwb dandisets')
    parser.add_argument('--test', default=False, action='store_true', help='only test 2 files in 10 dandisets')
    parser.add_argument('--update', default=False, action='store_true', help='only test non-tested dandisets')
    parser.add_argument('--succint', default=False, action='store_true',
                        help='return detailed report messages')
    args = parser.parse_args()
    validate_nwb(args.test,args.update, args.succint)
    update_readme()

'''
A script to get dandiset/individual nwb files based on user input. In development.
'''
import datalad.api as dl
import sys
import pandas as pd
import json

# TODO: file directories need to be made clear, otherwise install conflict

def get_nwb(dandiset_id):
    # print("NWB dataset to be examined:", str(sys.argv[1]))
    # nwb_dataset = sys.argv[1]
    dataset_path = input('Target directory')
    github_link_format = 'https://github.com/dandisets/'
    json_file = '.dandi/assets.json'

    dl.install(path=dataset_path,source=github_link_format+dandiset_id,recursive=True)

    # import json
    with open(json_file) as f:
      data = json.load(f)
    # flatten json file to pandas table
    json_df = pd.json_normalize(data)
    # only get individual file's path and size
    cols = ['path','size']
    json_df = json_df[cols]

    # print table here with total bytes info
    print('Files in dandiset and its size')
    print(json_df)
    pd.set_option('display.width',1000)
    pd.set_option('display.max_rows')

    # ask if user wants to download entire dataset or selective files
    total_bytes = json_df['size'].sum()
    ans = input('The dandiset is' + str(total_bytes) + 'bytes big. Do you want to download the dandiset or some of its files? (0:dandiset | 1: some files')
    # before downlooading, has to remove first because datalad doesn't install the dataset if folder is not empty
    dl.remove(path=os.path.join(dataset_path, 'dandisets', nwb_dataset))

    if ans == 0:
        dl.install(path=dataset_path, source=github_link_format + dataset_path, recursive=True, get_data=True)
    else:
        num_file = input('Number of files to download:')
        if num_file == 0:
            print('No files wanted. Exiting...')
            exit()

        file_path = input('Please specify the file path(s) as shown in the table. If multiple files, please separate them by commas.')
        try:
            nwb_file = list(file_path.strip().split(','))
        except:
            nwb_file = list(file_path)

        # need to check argument source
        for i in range(len(nwb_file)):
            dl.install(path=dataset_path,source=github_link_format+dataset_path+nwb_file[i], get_data=True)

# validate pynwb
# test.py nwb_filename

# test compatibility
# test_compatibility nwb_filename

if __name__ == "__main__":
    if len(sys.argv)==1:
        print('Please specify the dandiset you want (example input: 000xxx)')
        exit()

    get_nwb(str(sys.argv[1]))
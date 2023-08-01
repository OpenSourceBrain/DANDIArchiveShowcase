'''
This function is meant to be called from nwb_table_readme.py script to test NWBE compatibility
'''
import sys
import os

# import modules
from datetime import datetime, tzinfo, timedelta
#import hdmf._version
from dateutil.tz import tzlocal
import platform
import math
import numpy as np
import uuid
import os
from os import environ
import scipy.io as sio
from hdmf.backends.hdf5.h5_utils import H5DataIO
import pandas as pd
import plotly
import pynwb

from pynwb import NWBHDF5IO

#https://pypi.org/project/pyabf/
import pyabf

import pynwb


def create_summary(nwbfilepath,dandi_ident):
    
    # Step 0: Base variables
    save_folder = 'validation_folder' #if not path
    html_folder = 'summary'#if not path
    
    summary_file = os.path.join(save_folder, 'dandiset_summary.csv')
    
    dandi_metadata_readme = pd.read_csv(summary_file)
    dandi_metadata_readme.drop(dandi_metadata_readme.filter(regex="Unnamed"), axis=1, inplace=True)
    dandi_metadata_readme.to_csv(summary_file, index=False)
    
    dandi_metadata_readme.loc[:, 'identifier'] = [i.split(':')[1] for i in dandi_metadata_readme.loc[:, 'identifier']]
    
    dandi_path = os.path.join(html_folder,str(dandi_ident))
    html_temp = 'summary_template.html'
    dandi_metadata_readme['html_0'] = None
    dandi_metadata_readme['html_1'] = None 
    
    if not os.path.exists(dandi_path):
        os.makedirs(dandi_path)
    
    index = dandi_metadata_readme.index[dandi_metadata_readme.apply(lambda row: dandi_ident in row['identifier'], axis=1)].tolist()

    value_to_check = dandi_metadata_readme['html_0'][index].tolist()[0]
    
    if value_to_check == None:
        dandi_metadata_readme['html_0'][index] = 'file_0'
        html_path = os.path.join(dandi_path,'file_0')
    else:
        dandi_metadata_readme['html_1'][index] = 'file_1'
        html_path = os.path.join(dandi_path,'file_1')        
    
    
    # Step 1: Open the html file template and store it in base variable

    try:
        with open(html_temp, "r") as file:
            html_content = file.read()

    except FileNotFoundError:
        print(f"File '{html_temp}' not found.")
        html_content = ""

    html_variable = f"""{html_content}"""
    print(html_variable)
    
    # Step 2: Create html file for edit (add right dir, this is only for test)
    myfile = open(html_path, 'w')
    title = "Dandiset Summary"
    
    # Step 3: Add Metadata to HTML
    metadatatmpl = """<div class="metadata"><div class="left1">{title}</div><div class="right-column">{info}</div></div>"""
    
    message = ""
    
    print(dandi_metadata_readme['data_type'].iloc[index])
    
    if not pd.isna(dandi_metadata_readme['data_type'].iloc[index]).tolist()[0]:
       message+=metadatatmpl.format(title="Data Type",info=dandi_metadata_readme['data_type'].iloc[index].tolist()[0])

    if not pd.isna(dandi_metadata_readme['nwb_version'].iloc[index]).tolist()[0]:
       message+=metadatatmpl.format(title="NWB Version",info=dandi_metadata_readme['nwb_version'].iloc[index].tolist()[0])
       
    if not pd.isna(dandi_metadata_readme['num_bytes'].iloc[index]).tolist()[0]:
       message+=metadatatmpl.format(title="Total Size",info=str(round(int(dandi_metadata_readme['num_bytes'].iloc[index].tolist()[0])/1000000,2)))
       message+=metadatatmpl.format(title="Number of files",info=str(dandi_metadata_readme['num_files'].iloc[index].tolist()[0]))
       
    if not pd.isna(dandi_metadata_readme['species'].iloc[index]).tolist()[0]:
       message+=metadatatmpl.format(title="Species",info=dandi_metadata_readme['species'].iloc[index].tolist()[0])
    
    
    myfile.write(html_content.replace("{metadata}", message))
    myfile.close()

if __name__ == '__main__':
    create_summary(sys.argv[1],sys.argv[2])
    

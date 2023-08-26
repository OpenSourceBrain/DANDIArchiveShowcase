'''
This function is meant to be called from nwb_table_readme.py script to test NWBE compatibility
'''
import sys
import os

import heapq

import numpy as np
import matplotlib.pyplot as plt #add to docker

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
import pynwb

from pynwb import NWBHDF5IO

#https://pypi.org/project/pyabf/
#import pyabf
import signal
import subprocess
import pandas as pd
import yaml
import math
import datalad.api as dl
import json
import argparse
from datetime import date

from pynwb.image import ImageSeries
from pynwb.base import TimeSeries
from pynwb.behavior import BehavioralTimeSeries, BehavioralEvents
from dandi.pynwb_utils import get_nwb_version
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import save_report, format_messages, MessageFormatter
from dandi import download
import ast
from collections import Counter

def plot_and_save_timeseries(timeseries,path_to_save,image_tag,file_size):


    ts = timeseries
    file_path = os.path.join(path_to_save,f'plot_'+str(image_tag)+'.png')
    
    if isinstance(ts, TimeSeries):
        plt.figure()
        selected_trace = ts.data[:]
        if ts.timestamps is not None:
            num_timestamps = min(len(ts.timestamps), len(selected_trace))
        
            plt.plot(ts.timestamps[:num_timestamps], selected_trace[:num_timestamps]) 
            plt.xlabel('Time')
            plt.ylabel('Value')
            plt.title(f"Timeseries: {ts.name}")
            plt.savefig("temp.png", bbox_inches='tight')
            
            curr_file_size = os.path.getsize("temp.png")
            if curr_file_size > file_size:
                file_size = curr_file_size
                plt.savefig(file_path, bbox_inches='tight')
            #os.remove("temp.png")
                
            plt.close()
            
            return((file_size,image_tag))
        else:
            plt.plot(selected_trace) 
            plt.title(f"Timeseries: {ts.name}")
            plt.savefig("temp.png", bbox_inches='tight')

            curr_file_size = os.path.getsize("temp.png")
            if curr_file_size > file_size:
                file_size = curr_file_size
                plt.savefig(file_path, bbox_inches='tight')
            #os.remove("temp.png")
            plt.close()
            return((file_size,image_tag))
                
           
                
    return((file_size,image_tag))


def save_images_as_png(images,path_to_save,image_tag,file_size):
    
    file_path = os.path.join(path_to_save,f'image_'+str(image_tag)+'.png')
    
    for idx, image in enumerate(images):
        plt.imshow(image, cmap='gray')  # Assuming grayscale images
        plt.axis('off')
        
        plt.savefig("temp.png", bbox_inches='tight')    
        curr_file_size = os.path.getsize("temp.png")
        if curr_file_size > file_size:
            file_size = curr_file_size
            plt.savefig(file_path, bbox_inches='tight')
        plt.close()
        return((file_size,image_tag)) 
        
        
def scan_processing(obj,plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path):
    if isinstance(obj, ImageSeries):
        images_to_save = obj.data[:5]  
        if im_counter == 5:
            comp = heapq.heappop(image_pairs)
            temp = save_images_as_png(images_to_save,dandi_path,comp[1],comp[0])
            heapq.heappush(image_pairs, temp)
        else:
            temp = save_images_as_png(images_to_save,dandi_path,image_tag,0)
            image_tag=image_tag+1
            im_counter=im_counter+1
            heapq.heappush(image_pairs, temp)
            #print(f"Found images and saved them as PNG.")
            
           
    elif isinstance(obj, TimeSeries):
        if plot_counter == 5:
            comp = heapq.heappop(plot_pairs)
            temp = plot_and_save_timeseries(obj,dandi_path,comp[1],comp[0])
            heapq.heappush(plot_pairs, temp)
        else:
            temp = plot_and_save_timeseries(obj,dandi_path,plot_tag,0)
            plot_tag=plot_tag+1
            plot_counter=plot_counter+1
            heapq.heappush(plot_pairs, temp)  
            
def scan_acquisiton(obj,plot_pairs,plot_counter,plot_tag,dandi_path):
    if plot_counter == 5:
        comp = heapq.heappop(plot_pairs)
        temp = plot_and_save_timeseries(obj,dandi_path,comp[1],comp[0])
        heapq.heappush(plot_pairs, temp)
    else:
        temp = plot_and_save_timeseries(obj,dandi_path,plot_tag,0)
        plot_tag=plot_tag+1
        plot_counter=plot_counter+1
        heapq.heappush(plot_pairs, temp)            

                
def create_summary(nwb_path,dandi_ident,html_tag):
    # Step 0: Base variables
    save_folder = 'validation_folder' #if not path
    html_folder = 'Summaries'#if not path
    file_folder = 'file_'+str(html_tag)
    
    
    
    dandi_path = os.path.join(html_folder,os.path.join(str(dandi_ident),file_folder))
    
    html_temp = 'testing/summary_template.html' #add docker args
    
    html_path = os.path.join(dandi_path,'file_'+str(html_tag)+'.html')
    
    if not os.path.exists(dandi_path):
        os.makedirs(dandi_path)
    
    
    
    
    # Step 1: Open the html file template and store it in base variable

    try:
        with open(html_temp, "r") as file:
            html_content = file.read()

    except FileNotFoundError:
        print(f"File '{html_temp}' not found.")
        html_content = ""

    html_variable = f"""{html_content}"""
    
    # Step 2: Create html file for edit (add right dir, this is only for test)
    myfile = open(html_path, 'w')
    title = "Dandiset Summary"
    html_content = html_content.replace("{ident}", dandi_ident)
    #if not pd.isna(dandi_metadata_readme['name'].iloc[index]).tolist()[0]:
    #   html_content = html_content.replace("{dandi_desc}", dandi_metadata_readme['name'].iloc[index].tolist()[0])
    
    # Step 3: Add Metadata to HTML
    metadatatmpl = """<div><div>{title}</div><div>{info}</div></div>"""
    
    message = ""
    
    #print(dandi_metadata_readme['data_type'].iloc[index])
    
    #if not pd.isna(dandi_metadata_readme['data_type'].iloc[index]).tolist()[0]:
     #  message+=metadatatmpl.format(title="Data Type",info=dandi_metadata_readme['data_type'].iloc[index].tolist()[0])

    #if not pd.isna(dandi_metadata_readme['nwb_version'].iloc[index]).tolist()[0]:
    #   message+=metadatatmpl.format(title="NWB Version",info=dandi_metadata_readme['nwb_version'].iloc[index].tolist()[0])
       
    #if not pd.isna(dandi_metadata_readme['num_bytes'].iloc[index]).tolist()[0]:
     #  message+=metadatatmpl.format(title="Total Size",info=str(round(int(dandi_metadata_readme['num_bytes'].iloc[index].tolist()[0])/1000000,2)))
     #  message+=metadatatmpl.format(title="Number of files",info=str(dandi_metadata_readme['num_files'].iloc[index].tolist()[0]))
       
    #if not pd.isna(dandi_metadata_readme['species'].iloc[index]).tolist()[0]:
     #  message+=metadatatmpl.format(title="Species",info=dandi_metadata_readme['species'].iloc[index].tolist()[0])
    
    
    html_content = html_content.replace("{metadata}", message)
    
    
    # Adding plots for timeseries -----------------------------------------
    
    io = NWBHDF5IO(nwb_path,mode='r',load_namespaces=True) # Add try except block
    nwbfile = io.read()
    nwbe_compatibility = 'p-0'
    type_hierarchy = set([ImageSeries,TimeSeries,BehavioralTimeSeries,BehavioralEvents])
    plottable = 0
    message = ""
    
    for a, v in nwbfile.acquisition.items():
        print(nwbfile.acquisition[a].neurodata_type)
        if len(set(nwbfile.acquisition[a].type_hierarchy()).intersection(type_hierarchy)) >= 1:
            if ImageSeries in nwbfile.acquisition[a].type_hierarchy():
                pass
            else:
                nwbe_compatibility = 'p-1'
                plottable = 1
                break
    if plottable == 0:
        for a, v in nwbfile.processing.items():
            print(nwbfile.processing[a].neurodata_type)
            if len(set(nwbfile.processing[a].type_hierarchy()).intersection(type_hierarchy)) >= 1:
                if ImageSeries in nwbfile.processing[a].type_hierarchy():
                    pass
                else:
                    nwbe_compatibility = 'p-2'
                    plottable = 1
                    break
    
        
    
    image_tmpl = """<h5>{title}</h5><img src="{path}" alt="Image">"""
    
    plot_pairs = []
    image_pairs = []
    
    heapq.heapify(plot_pairs)
    heapq.heapify(image_pairs)
    
    plot_counter = 0
    im_counter = 0
    
    plot_tag = 1
    image_tag = 1

    for processing_module_name in nwbfile.processing:
        for p2 in nwbfile.processing[processing_module_name].data_interfaces:
            try:
                for field in nwbfile.processing[processing_module_name].data_interfaces[p2].time_series:
                    print(field)
                    #scan_processing(nwbfile.processing[processing_module_name].data_interfaces[p2].time_series[field],plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)
                    if isinstance(nwbfile.processing[processing_module_name].data_interfaces[p2].time_series[field], ImageSeries):
                        images_to_save = nwbfile.processing[processing_module_name].data_interfaces[p2].time_series[field].data[:5]  
                        if im_counter == 5:
                            comp = heapq.heappop(image_pairs)
                            temp = save_images_as_png(images_to_save,dandi_path,comp[1],comp[0])
                            print(temp[1])
                            heapq.heappush(image_pairs, temp)
                        else:
                            temp = save_images_as_png(images_to_save,dandi_path,image_tag,0)
                            image_tag=image_tag+1
                            im_counter=im_counter+1
                            heapq.heappush(image_pairs, temp)
            #print(f"Found images and saved them as PNG.")
            
           
                    elif isinstance(nwbfile.processing[processing_module_name].data_interfaces[p2].time_series[field], TimeSeries):
                        if plot_counter == 5:
                            comp = heapq.heappop(plot_pairs)
                            temp = plot_and_save_timeseries(nwbfile.processing[processing_module_name].data_interfaces[p2].time_series[field],dandi_path,comp[1],comp[0])
                            print(temp[1])
                            heapq.heappush(plot_pairs, temp)
                        else:
                            temp = plot_and_save_timeseries(nwbfile.processing[processing_module_name].data_interfaces[p2].time_series[field],dandi_path,plot_tag,0)
                            plot_tag=plot_tag+1
                            plot_counter=plot_counter+1
                            heapq.heappush(plot_pairs, temp)  
                print(plot_counter)
            except:
                print("failed")
                #scan_processing(nwbfile.processing[processing_module_name].data_interfaces,plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)
                if isinstance(nwbfile.processing[processing_module_name].data_interfaces, ImageSeries):
                    images_to_save = nwbfile.processing[processing_module_name].data_interfaces.data[:5]  
                    if im_counter == 5:
                        comp = heapq.heappop(image_pairs)
                        temp = save_images_as_png(images_to_save,dandi_path,comp[1],comp[0])
                        print(temp[1])
                        heapq.heappush(image_pairs, temp)
                    else:
                        temp = save_images_as_png(images_to_save,dandi_path,image_tag,0)
                        image_tag=image_tag+1
                        im_counter=im_counter+1
                        heapq.heappush(image_pairs, temp)
            #print(f"Found images and saved them as PNG.")
            
           
                elif isinstance(nwbfile.processing[processing_module_name].data_interfaces, TimeSeries):
                    if plot_counter == 5:
                        comp = heapq.heappop(plot_pairs)
                        temp = plot_and_save_timeseries(nwbfile.processing[processing_module_name].data_interfaces,dandi_path,comp[1],comp[0])
                        print(temp[1])
                        heapq.heappush(plot_pairs, temp)
                    else:
                        temp = plot_and_save_timeseries(nwbfile.processing[processing_module_name].data_interfaces,dandi_path,plot_tag,0)
                        plot_tag=plot_tag+1
                        plot_counter=plot_counter+1
                        heapq.heappush(plot_pairs, temp)  
                        
                print(plot_counter)
            
    for processing_module_name in nwbfile.acquisition:
        try:
              for field in nwbfile.acquisition[processing_module_name].time_series:
                  print(field)
                  #scan_processing(nwbfile.acquisition[processing_module_name].time_series[field],plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)
                  if plot_counter == 5:
                      comp = heapq.heappop(plot_pairs)
                      temp = plot_and_save_timeseries(nwbfile.acquisition[processing_module_name].time_series[field],dandi_path,comp[1],comp[0])
                      print(temp[1])
                      heapq.heappush(plot_pairs, temp)
                  else:
                      temp = plot_and_save_timeseries(nwbfile.acquisition[processing_module_name].time_series[field],dandi_path,plot_tag,0)
                      plot_tag=plot_tag+1
                      plot_counter=plot_counter+1
                      heapq.heappush(plot_pairs, temp) 
                  print(plot_counter)
        except:
            print("failed")
            #scan_processing(nwbfile.acquisition[processing_module_name],plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)
            if plot_counter == 5:
                comp = heapq.heappop(plot_pairs)
                temp = plot_and_save_timeseries(nwbfile.acquisition[processing_module_name],dandi_path,comp[1],comp[0])
                print(temp[1])
                heapq.heappush(plot_pairs, temp)
            else:
                temp = plot_and_save_timeseries(nwbfile.acquisition[processing_module_name],dandi_path,plot_tag,0)
                plot_tag=plot_tag+1
                plot_counter=plot_counter+1
                heapq.heappush(plot_pairs, temp) 
                print(plot_counter)
                
    for processing_module_name in nwbfile.stimulus:
        try:
              for field in nwbfile.stimulus[processing_module_name].time_series:
                  print(field)
                  #scan_processing(nwbfile.acquisition[processing_module_name].time_series[field],plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)
                  if plot_counter == 5:
                      comp = heapq.heappop(plot_pairs)
                      temp = plot_and_save_timeseries(nwbfile.stimulus[processing_module_name].time_series[field],dandi_path,comp[1],comp[0])
                      print(temp[1])
                      heapq.heappush(plot_pairs, temp)
                  else:
                      temp = plot_and_save_timeseries(nwbfile.stimulus[processing_module_name].time_series[field],dandi_path,plot_tag,0)
                      plot_tag=plot_tag+1
                      plot_counter=plot_counter+1
                      heapq.heappush(plot_pairs, temp) 
                  print(plot_counter)
        except:
            print("failed")
            #scan_processing(nwbfile.acquisition[processing_module_name],plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)
            if plot_counter == 5:
                comp = heapq.heappop(plot_pairs)
                temp = plot_and_save_timeseries(nwbfile.stimulus[processing_module_name],dandi_path,comp[1],comp[0])
                print(temp[1])
                heapq.heappush(plot_pairs, temp)
            else:
                temp = plot_and_save_timeseries(nwbfile.stimulus[processing_module_name],dandi_path,plot_tag,0)
                plot_tag=plot_tag+1
                plot_counter=plot_counter+1
                heapq.heappush(plot_pairs, temp) 
                print(plot_counter)
        
    if(os.path.exists("temp.png")):
        os.remove("temp.png")
    io.close()
    
    if len(os.listdir(dandi_path))>1 :
        for file_name in sorted(os.listdir(dandi_path)):
            if file_name.startswith("image"):
                message+=image_tmpl.format(title=file_name,path=file_name)
            elif file_name.startswith("plot"):
                message+=image_tmpl.format(title=file_name,path=file_name)
    else:
        #os.remove(os.path.join(dandi_path,'html_'+str(html_tag)+'.html'))
        raise Exception("Data couldn't be accessed .") 
    print(message)                 
                
    html_content = html_content.replace("{Plots}", message)
           
    
    # --------------------------------------------------------------------------
    
    #value_to_check = dandi_metadata_readme['html_0'][index].tolist()[0]
    
    #if value_to_check == None:
     #   dandi_metadata_readme['html_0'][index] = 'file_0'
      #  html_path = os.path.join(dandi_path,'file_0.html')
    #else:
     #   dandi_metadata_readme['html_1'][index] = 'file_1'
      #  html_path = os.path.join(dandi_path,'file_1.html') 
    
    myfile.write(html_content)
    myfile.close()
    
    print(nwbe_compatibility)
    
if __name__ == '__main__':
    create_summary(sys.argv[1],sys.argv[2],sys.argv[3])
    

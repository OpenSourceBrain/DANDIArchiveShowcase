'''
This function is meant to be called from nwb_table_readme.py script to test NWBE compatibility
'''
import sys
import os

import heapq

import numpy as np
import matplotlib.pyplot as plt #add to docker

import math
from hdmf.backends.hdf5.h5_utils import H5DataIO
import pandas as pd
import pynwb
from pynwb import NWBHDF5IO

from pynwb.image import ImageSeries
from pynwb.base import TimeSeries
from pynwb.behavior import BehavioralTimeSeries, BehavioralEvents
from dandi.pynwb_utils import get_nwb_version
from nwbinspector import inspect_nwb
from nwbinspector.register_checks import Importance
from nwbinspector.inspector_tools import save_report, format_messages, MessageFormatter
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
            
    return(plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag)
            
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
    
    return(plot_pairs,plot_counter,plot_tag)         

                
def create_summary(nwb_path,dandi_ident,html_tag):
    # Step 0: Base variables
    save_folder = 'testing/validation_folder'
    html_folder = os.path.join(save_folder,'Summaries')
    file_folder = 'file_'+str(html_tag)
    
    
    
    dandi_path = os.path.join(html_folder,os.path.join(str(dandi_ident),file_folder))
    
    html_temp = 'testing/summary_template.html' #add docker args
    
    html_path = os.path.join(dandi_path,'README.md')
    
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

    
    # Step 3: Add Metadata to HTML
    metadatatmpl = """<div><div>{title}</div><div>{info}</div></div>"""
    

    
    
    
    html_content = html_content.replace("{file_name}",nwb_path.split('/')[-1])
    
    
    # Adding plots for timeseries -----------------------------------------
    
    io = NWBHDF5IO(nwb_path,mode='r',load_namespaces=True) # Add try except block
    nwbfile = io.read()
    
    image_html = ""
    plots_html = ""
    
    image_tmpl = """<img src="{path}" alt="Image">"""
    
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
                    plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag = scan_processing(nwbfile.processing[processing_module_name].data_interfaces[p2].time_series[field],plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)

            except:
                plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag = scan_processing(nwbfile.processing[processing_module_name].data_interfaces,plot_pairs,image_pairs,plot_counter,im_counter,plot_tag,image_tag,dandi_path)
            
    for processing_module_name in nwbfile.acquisition:
        try:
              for field in nwbfile.acquisition[processing_module_name].time_series:
                  plot_pairs,plot_counter,plot_tag = scan_acquisiton(nwbfile.acquisition[processing_module_name].time_series[field],plot_pairs,plot_counter,plot_tag,dandi_path)
        except:
            plot_pairs,plot_counter,plot_tag = scan_acquisiton(nwbfile.acquisition[processing_module_name],plot_pairs,plot_counter,plot_tag,dandi_path)
                
    for processing_module_name in nwbfile.stimulus:
        try:
              for field in nwbfile.stimulus[processing_module_name].time_series:
                  plot_pairs,plot_counter,plot_tag = scan_acquisiton(nwbfile.stimulus[processing_module_name].time_series[field],plot_pairs,plot_counter,plot_tag,dandi_path)

        except:
            plot_pairs,plot_counter,plot_tag = scan_acquisiton(nwbfile.stimulus[processing_module_name],plot_pairs,plot_counter,plot_tag,dandi_path)
        
    if(os.path.exists("temp.png")):
        os.remove("temp.png")
    io.close()
    
    if len(os.listdir(dandi_path))>1 :
        for file_name in sorted(os.listdir(dandi_path)):
            if file_name.startswith("image"):
                image_html+=image_tmpl.format(path=file_name)
            elif file_name.startswith("plot"):
                plots_html+=image_tmpl.format(path=file_name)
    else:
        raise Exception("Data couldn't be accessed .") 
                
    if plots_html != "":
        html_content = html_content.replace("{Plots}", plots_html)
    else:
        html_content = html_content.replace("{Plots}", "No Plots Were Found !")
         
    if image_html != "":
        html_content = html_content.replace("{Images}", image_html)
    else:
        html_content = html_content.replace("{Images}", "No Images Were Found !")
           
    
    # --------------------------------------------------------------------------
    
    myfile.write(html_content)
    myfile.close()
    
if __name__ == '__main__':
    create_summary(sys.argv[1],sys.argv[2],sys.argv[3])
    

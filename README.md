# DANDI Archive Showcase

Scripts for interacting with the [DANDI Archive](https://www.dandiarchive.org/), particularly from [OSBv2](https://docs.opensourcebrain.org/OSBv2/Overview.html).

**Summary statistics about numbers and validity of NWB files across all dandisets can be found [here](validation_folder/README.md), along with an indication about compatibility with NWB Explorer.**

## Installation Instructions 
The scripts in this repo work best in an
[Anaconda](https://www.anaconda.com/distribution/#download-section) environment, and [git](https://git-scm.com/downloads) is required for running one of the packages, 
so please make sure they are installed and added to the system path. 
In addition, a local installation of NWB Explorer is advised for the purpose of testing files' compatibility with the app.
For details on NWBE's installation requirements and instructions, please visit [here]((https://github.com/MetaCell/nwb-explorer)) 

In your git terminal, navigate to the directory in which you want to clone the DANDIArchiveSHOWCASE repo. Run the following commands:

```commandline
conda create --name dandiarchiveshowcase python=3.9 --yes
conda activate dandiarchiveshowcase
conda install --channel conda-forge datalad h5py
git clone https://github.com/OpenSourceBrain/DANDIArchiveShowcase
git clone --branch development https://github.com/MetaCell/nwb-explorer
pip install --requirement DANDIArchiveShowcase/requirements.txt
pip install --editable nwb-explorer
python nwb-explorer/utilities/install.py
cd DANDIArchiveShowcase
```

## Scripts information
- The nwb_table_readme.py script allows users to parse through all the dandisets in DANDIArchive, extract metadata information
and validate files in each dandiset against NWBInspector, as well as testing their compatibility with NWB Explorer. 
Validation reports and summary information are saved in a directory called validation_folder.
- The compatibility_test.py script works as a companion script to nwb_table_readme.py for the purpose of inspecting a file's compatibility with NWBE.
```
nwb_table_readme.py
Usage: python nwb_table_readme.py [OPTIONS]

  Parse through all the dandisets in DANDIArchive, extract metadata information and
   validate files in each dandiset using NWBInspector.
   
Options:
  --no_download                 Files will not be downloaded for testing if so chosen
  --no_sizelimit                No size limit will be capped for downloading files if so chosen
  --dandiset_limit              Only process first 10 dandisets if so chosen'
  --update_readme_option        Update readme file after summary file is created
  --update_readme_only          Update readme file without creating summary file
  --test_docker                 (Test Dandisets / Update Readme) using the NWBE container
  --create_summary              Create summaries for files which do not contain one
```
- The get_nwb.py script is an interactive shell script that allows users to install dandisets or files from dandisets via [Datalad](https://github.com/datalad/datalad), 
and validate the files with [NWBInspector](https://github.com/NeurodataWithoutBorders/nwbinspector) as they wish.
```
get_nwb.py
Usage: python get_nwb.py [Dandiset identifier (eg: 000003)]

  Clone and install a dandiset/files from a dandiset via Datalad. NWBInspector is called to validate files if so chosen.
```
- The nwbinspector_bulk.py script allows users to validate files in the NWBShowcase repository or a local directory in bulk. 
Validation reports are saved in a directory called validation_folder/nwbinspector_bulk
```
nwbinspector_bulk.py
Usage: python nwbinspector_bulk.py [OPTIONS]

  Validate files in the NWBShowcase repository with NWBInspector as default.

Options:
  --folder_path                 Files from a provided local directory will be validated with NWBInspector
```








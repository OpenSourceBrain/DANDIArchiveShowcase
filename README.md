# DANDI Archive Showcase

Scripts for interacting with the [DANDI Archive](https://www.dandiarchive.org/), particularly from [OSBv2](https://docs.opensourcebrain.org/OSBv2/Overview.html).
 For information about the NWB dandisets that is generated by the scripts in this repo, please visit [here](validation_folder/README.md).

## Installation instruction
The scripts in this repo work best in an
[Anaconda](https://www.anaconda.com/distribution/#download-section) environment, and [git](https://git-scm.com/downloads) is required for running one of the packages, 
so please make sure they are installed and added to the system path.

In your git terminal, navigate to the directory in which you want to install the DandiArchiveSHOWCASE repo. Run the following commands:

```commandline
conda create --name dandiarchiveshowcase python=3.9 --yes
conda activate dandiarchiveshowcase
git clone https://github.com/OpenSourceBrain/DANDIArchiveShowcase
conda install -c conda-forge datalad
pip install --requirement requirements.txt
```

## Scripts information
The nwb_table_readme.py script allows one to parse through all the dandisets in DANDIArchive, extract metadata information
and validate files in each dandiset against NWBInspector. Further development will enable the script to test files/dandisets' compatibility
with NWB Explorer. Validation results and summary information are saved in a directory called validation_folder.
```
nwb_table_readme.py
Usage: python nwb_table_readme.py [OPTIONS]

  Parse through all the dandisets in DANDIArchive, extract metadata information and
   validate files in each dandiset against NWBInspector.
   
Options:
  --no_download                 Files will not be downloaded for testing if so chosen
  --no_sizelimit                No size limit will be capped for downloading files if so chosen
  --dandiset_limit              Only process first 10 dandisets if so chosen'
  --update_readme_option        Update readme file after summary file is created
  --update_readme_only          Update readme file without creating summary file
```
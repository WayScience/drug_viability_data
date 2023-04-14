#!/usr/bin/env python
# coding: utf-8

# ## Download NCI-60 Growth Inhibition Data
# 
# https://wiki.nci.nih.gov/display/NCIDTPdata/NCI-60+Growth+Inhibition+Data
# 
# 71 Cell Lines treated with 57,000 compounds
# 
# The notebook downloads two files:
# 
# 1. Dose response data (April 2023 release)
# 2. Chemical name dictionary

# In[1]:


import pathlib
import sys

sys.path.append("../")
from utils import download_utils


# In[2]:


# Construct output directory
output_dir = pathlib.Path("data")
output_dir.mkdir(exist_ok=True)


# In[3]:


# Base url for downloading NCI-60 data
nci_url = "https://wiki.nci.nih.gov/download/attachments/"


# In[4]:


# Download the dose response data
attachment_id = "147193864"
attachment_name = "DOSERESP.zip"
data_version = "7"  # April 2023
modification_date = "1680574847000"
api_version = "v2"
output_file = pathlib.Path(output_dir, attachment_name)

download_utils.download_nci60(
    output_file=output_file,
    base_url=nci_url,
    attachment_id=attachment_id,
    attachment_name=attachment_name,
    data_version=data_version,
    modification_date=modification_date,
    api_version=api_version,
    extract_zip=True,
)


# In[5]:


# Download the chemical dictionary
attachment_id = "155844992"

# Note, this is a text file, not actually a zip file
attachment_name = "chemnames_Aug2013.zip"
data_version = "1"
modification_date = "1378214926000"
api_version = "v2"
output_file = pathlib.Path(output_dir, attachment_name)

download_utils.download_nci60(
    output_file=output_file,
    base_url=nci_url,
    attachment_id=attachment_id,
    attachment_name=attachment_name,
    data_version=data_version,
    modification_date=modification_date,
    api_version=api_version,
    extract_zip=False,
)


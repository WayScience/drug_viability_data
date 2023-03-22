#!/usr/bin/env python
# coding: utf-8

# ## Download NCI-60 Growth Inhibition Data
# 
# https://wiki.nci.nih.gov/display/NCIDTPdata/NCI-60+Growth+Inhibition+Data
# 
# 71 Cell Lines treated with 57,000 compounds

# In[1]:


import pathlib
import pandas as pd

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
version = "6"
modification_date = "1672801037000"
api = "v2"
output_file = pathlib.Path(output_dir, attachment_name)

download_utils.download_nci60(
    output_file=output_file,
    base_url=nci_url,
    attachment_id=attachment_id,
    attachment_name=attachment_name,
    version=version,
    modification_date=modification_date,
    api=api,
    extract_zip=True,
)


# In[5]:


# Download the chemical dictionary
attachment_id = "155844992"
attachment_name = "chemnames_Aug2013.zip"  # Note, not actually a zip file
version = "1"
modification_date = "1378214926000"
api = "v2"
output_file = pathlib.Path(output_dir, attachment_name)

download_utils.download_nci60(
    output_file=output_file,
    base_url=nci_url,
    attachment_id=attachment_id,
    attachment_name=attachment_name,
    version=version,
    modification_date=modification_date,
    api=api,
    extract_zip=False,
)


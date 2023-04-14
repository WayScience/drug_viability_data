#!/usr/bin/env python
# coding: utf-8

# ## Download CCLE Drug Viability Data
# 
# Source: [DepMap portal](https://depmap.org/portal/download/) (Pharmacological Profiling)
# 
# We download the file `CCLE_NP24.2009_Drug_data_2015.02.24.csv`

# In[1]:


import sys

sys.path.append("../")
from utils import download_utils


# In[2]:


output_dir = "data"

file_name = "CCLE_NP24.2009_Drug_data_2015.02.24.csv"
bucket = "depmap-external-downloads"
resource = "pharmacological_profiling"


# In[3]:


download_utils.download_depmap_bucket(
    file_name=file_name, output_dir=output_dir, bucket=bucket, resource=resource
)


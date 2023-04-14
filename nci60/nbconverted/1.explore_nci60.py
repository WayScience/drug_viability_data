#!/usr/bin/env python
# coding: utf-8

# ## Explore NCI-60 data
# 
# There are two screens:
# 
# - Primary screen
# - Secondary screen

# In[1]:


import pathlib
import sys

import pandas as pd

sys.path.append("../")
from utils import load_utils


# In[2]:


# Load NCI60 data (primary screen)
top_dir = ".."
data_dir = "nci60/data"

nci60_df, nci60_trt_df = load_utils.load_nci60(
    top_dir=top_dir, data_dir=data_dir, load_treatment_info=True
)

print(nci60_df.shape)
nci60_df.head(3)


# In[3]:


print(nci60_trt_df.shape)
nci60_trt_df.head(3)


# In[4]:


# How many unique cell lines?
print(nci60_df.nunique())
nci60_df.CELL_NAME.value_counts().head(20)


# In[5]:


# How many unique compounds?
print(nci60_trt_df.nsc_number.nunique())


# In[6]:


# Compounds are annotated to different name types
# Print different examples of cpd name types
nci60_trt_df.cpd_name_type.value_counts()


# In[7]:


# How many doses?
# (Note: -log10 value)
nci60_df.CONCENTRATION.value_counts()


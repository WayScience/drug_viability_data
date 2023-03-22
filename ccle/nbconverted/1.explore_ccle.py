#!/usr/bin/env python
# coding: utf-8

# ## Describe Cancer Cell Line Encyclopedia Data

# In[1]:


import pathlib
import sys

import pandas as pd

sys.path.append("../")
from utils import load_utils


# In[2]:


# Load CCLE data
top_dir = ".."
data_dir = "ccle/data"

ccle_df = load_utils.load_ccle(top_dir=top_dir, data_dir=data_dir, process_tissues=True)

print(ccle_df.shape)
ccle_df.head(3)


# In[3]:


# How many cell lines
ccle_df.loc[:, "CCLE Cell Line Name"].value_counts()


# In[4]:


# How many unique perturbations
print(ccle_df.Compound.nunique())

ccle_df.Compound.value_counts()


# In[5]:


# How many tissues
print(ccle_df.tissue.nunique())

ccle_df.tissue.value_counts()


# In[6]:


# How many unique cell lines per tissue?
ccle_df.drop_duplicates(subset="cell_line_clean").tissue.value_counts()


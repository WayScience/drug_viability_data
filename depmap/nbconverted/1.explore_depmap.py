#!/usr/bin/env python
# coding: utf-8

# ## Describe Cancer Dependency Map Data

# In[1]:


import pathlib
import sys

sys.path.append("../")
from utils import load_utils


# In[2]:


# Load depmap data
top_dir = ".."
data_dir = "depmap/data"

depmap_df, depmap_cell_df, depmap_gene_df = load_utils.load_depmap(
    top_dir=top_dir, data_dir=data_dir, load_cell_info=True, load_gene_info=True
)

print(depmap_df.shape)
depmap_df.head(3)


# In[3]:


print(depmap_cell_df.shape)
depmap_cell_df.head(3)


# In[4]:


print(depmap_gene_df.shape)
depmap_gene_df.head(3)


# In[5]:


# How many tissues
depmap_cell_df.tissue.value_counts()


# In[6]:


# What are the diseases
print(depmap_cell_df.Cellosaurus_NCIt_disease.nunique())
depmap_cell_df.Cellosaurus_NCIt_disease.value_counts().head(20)


# In[7]:


# What are the sex distribution
depmap_cell_df.sex.value_counts()


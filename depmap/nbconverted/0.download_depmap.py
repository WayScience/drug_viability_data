#!/usr/bin/env python
# coding: utf-8

# ## Download Dependency Data
# 
# Source: [Cancer Dependency Map resource](https://depmap.org/portal/download/).
# 
# - CRISPRGeneDependency.csv: The data in this document describes the probability that a gene knockdown has an effect on cell-inhibition or death. These probabilities are derived from the data contained in CRISPRGeneEffect.csv using methods described [here](https://www.biorxiv.org/content/10.1101/720243v1).
# - Model.csv: Metadata for all of DepMap’s cancer models/cell lines.
# 
# We also create a gene dictionary for future lookups and recoding

# In[1]:


import pathlib
import urllib
import pandas as pd

import sys

sys.path.append("../")
from utils import download_utils, load_utils


# In[2]:


# Set output directory
output_dir = pathlib.Path("data")

# Make sure directory exists
output_dir.mkdir(exist_ok=True)

# Set output gene file
output_gene_dictionary = pathlib.Path(output_dir, "depmap_gene_dictionary.tsv")

# Set download constants
figshare_url = "https://ndownloader.figshare.com/files/"

download_dict = {"34990033": "CRISPRGeneDependency.csv", "35020903": "Model.csv"}


# In[3]:


for figshare_id in download_dict:
    # Set output file
    output_file = pathlib.Path(output_dir, download_dict[figshare_id])

    # Download the dependency data
    print(f"Downloading {output_file}...")

    download_utils.download_figshare(
        figshare_id=figshare_id, output_file=output_file, figshare_url=figshare_url
    )


# ## Process gene dictionary

# In[4]:


# Load the GeneDependency data that was just downloaded
top_dir = ".."
data_dir = "depmap/data"

depmap_df = load_utils.load_depmap(top_dir=top_dir, data_dir=data_dir)

print(depmap_df.shape)
depmap_df.head(3)


# In[5]:


# The columns are of the format: symbol (NCBI Entrez ID)
# Transform them and write out the dictionary
genes = depmap_df.columns[1:].tolist()

gene_data = []
for gene in genes:
    gene_name, ncbi_entrez_gene = gene.split(" ")
    gene_data.append([gene, gene_name, ncbi_entrez_gene.strip("()")])

gene_df = pd.DataFrame(
    gene_data, columns=["depmap_column_name", "gene_symbol", "ncbi_entrez_id"]
)

gene_df.to_csv(output_gene_dictionary, sep="\t", index=False)

print(gene_df.shape)
gene_df.head(3)


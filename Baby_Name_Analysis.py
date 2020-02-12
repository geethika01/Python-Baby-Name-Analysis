# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:27:03 2020

@author: Geethika.Wijewardena
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp
import seaborn
import zipfile as zp
import os
import glob

# Extraxt data from zip file
zp.ZipFile('names.zip').extractall('.')

# Read the first file and create a dataframe (df)
filename = glob.glob('*.txt')[0]
dat = pd.read_csv(filename, names= ['babyname', 'sex', 'count'], na_values = '')
dat['year'] = filename[3:7]

# Read the rest of the files and append data to df
for i in range(1,len(glob.glob('*.txt'))):
    #i = 1
    filename = glob.glob('*.txt')[i]
    newdat = pd.read_csv(filename, names= ['babyname', 'sex', 'count'], na_values = '')
    newdat['year'] = filename[3:7]
    dat = dat.append(newdat)

# Check for the null values    
dat.info(verbose = True, null_counts = True)



    

    


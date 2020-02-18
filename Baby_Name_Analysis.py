# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:27:03 2020

@author: Geethika.Wijewardena
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp
import seaborn as sns
import zipfile as zp
import os
import glob

# Extraxt data from zip file
#zp.ZipFile('names.zip').extractall('.')

os.chdir('names')

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

# count unique names
names_unique = dat.babyname.unique()

#-----------------------------------------------
# 1. For selected names get the count each year
#-----------------------------------------------

names_lst = ['Mary', 'Linda', 'Jennifer', 'Ashley', 'Deborah']

# Filter the dat by the given names
dat_selected = dat[dat['babyname'].isin(names_lst )]

# Plot data 
g = sns.lineplot('year', 'count', 'babyname', data = dat_selected, legend = 'full')
pp.show()

#-------------------------------------------------------------------
# 2. From the data set select the most popular names over 135 years
#--------------------------------------------------------------------



pp.plot('year','count', data=dat_selected, c='babyname')


def plotCountByYearOfName (name, sex):
    
    # Filter data by sex
    dat_sex = dat[dat['sex']== sex]
    
    # Filter by name
    dat_name = dat_sex[dat_sex['babyname']==name]
    
    # Plot data
    pp.plot(df_name['year'], df_name['count'])


plotCountByYearOfName('Mary', 'F')
pp.figure(figsize = (12, 2.5))



for name in names_lst:
    plotCountByYearOfName(name, 'F')
    
pp.legend(names_lst)




    

    


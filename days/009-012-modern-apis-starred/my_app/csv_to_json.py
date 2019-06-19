#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:44:51 2019

@author: tstone
"""

#Convert csv file to json

#Import data from csv file to a list file. 
import pandas as pd

#importing data from csv file 
data = pd.read_csv('marvel-wikia-data.csv')

#This is because I used data_test to make the conversion. 
data_test = data.copy()

#Taking the number of rows to iterate through
rows = data_test.shape[0]

#Create an empty dictionary file
dict_test = {}

#Iterate through each row to create a new dictionary file
for r in range(0,rows):
    tmp = data_test.iloc[r]
    try:
        dict_test[int(tmp['page_id'])] = {'id':int(tmp['page_id']),
             'name':str(tmp['name']),
             'urlslug':str(tmp['urlslug']),
             'ID':str(tmp['ID']),
             'ALIGN':str(tmp['ALIGN']), 
             'EYE':str(tmp['EYE']), 
             'HAIR':str(tmp['HAIR']),
             'SEX':str(tmp['SEX']),
             'GSM':str(tmp['GSM']),
             'ALIVE':str(tmp['ALIVE']),
             'APPEARANCES':str(tmp['APPEARANCES']),
             'FIRST APPEARANCE':str(tmp['FIRST APPEARANCE']),
             'Year':int(tmp['Year'])}
    except ValueError:
        dict_test[int(tmp['page_id'])] = {'id':int(tmp['page_id']),
             'name':str(tmp['name']),
             'urlslug':str(tmp['urlslug']),
             'ID':str(tmp['ID']),
             'ALIGN':str(tmp['ALIGN']), 
             'EYE':str(tmp['EYE']), 
             'HAIR':str(tmp['HAIR']),
             'SEX':str(tmp['SEX']),
             'GSM':str(tmp['GSM']),
             'ALIVE':str(tmp['ALIVE']),
             'APPEARANCES':str(tmp['APPEARANCES']),
             'FIRST APPEARANCE':str(tmp['FIRST APPEARANCE']),
             'Year':0}

import json

#Write to file
with open('marvel-wikia-data.json','w') as file:
    file.write(json.dumps(dict_test,indent=4))

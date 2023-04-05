# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 00:08:55 2023

@author: icterguru
"""


import pandas as pd
df = pd.read_csv('2019-Nov.csv', nrows=1000)
print (df);


df3 = pd.read_csv('2019-Nov.csv', chunksize=10000)

output = pd.DataFrame()
for chunk in df3:
    categories = ['brand','category_code','event_type']
    details = chunk[categories]
    #details['count'] = 1
    summary = details.groupby(categories).sum().reset_index()
    output = output.append(summary, ignore_index=True)

final_output = output.groupby(categories).sum().reset_index()
final_output.to_csv('summarized-consumer-info-2019-Nov.csv', index=False)
 
	 
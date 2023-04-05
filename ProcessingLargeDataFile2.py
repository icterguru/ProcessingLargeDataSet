# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 00:08:55 2023

@author: icterguru
"""

## Data File Source
#https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store/


import pandas as pd

df = pd.read_csv('2019-Nov.csv', nrows=100000, skiprows=1000)
#print (df);
df.columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
print(df);

consizedResult = pd.Series([], dtype="float64");
consizedResult = pd.concat([consizedResult, df.C/df.G]);
#consizedResult = pd.concat([consizedResult, df.G]);
print(df.C, df.G );
print(consizedResult);


print("With chunk ========================== ");
# https://www.youtube.com/watch?v=xtFo1IiZqzM

counter = 0;
output = pd.DataFrame()
df2 = pd.read_csv('2019-Nov.csv', chunksize= 1000000)
chunkedResult = pd.Series([], dtype="float64");

for chunk in df2:
    chunk.columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    chunkedResult = pd.concat([chunkedResult, chunk.C/chunk.G]);
    print ("counter = ", counter);
    counter += 1;
    
print(chunk.C, chunk.G );
print(chunkedResult);


print("--- - - -  - - -Generating a summarized file - - -  - - - -");

df3 = pd.read_csv('2019-Nov.csv', chunksize=1000000)

output = pd.DataFrame()
for chunk in df3:
    categories = ['brand','category_code','event_type']
    details = chunk[categories]
    details['count'] = 1
    summary = details.groupby(categories).sum().reset_index()
    output = output.append(summary, ignore_index=True)

final_output = output.groupby(categories).sum().reset_index()
final_output.to_csv('summarized-consumer-info-2019-Nov.csv', index=False)
 

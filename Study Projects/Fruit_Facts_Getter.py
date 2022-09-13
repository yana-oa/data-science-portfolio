# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:28:34 2022
FRUIT FACTS PROGRAM
@author: arian
"""

"""
This program will:
    Return the scientific name of an inputted fruit.
"""
#importing packages
import requests
import pandas as pd
import json

#First created response object and convert json to dict
fv_data = requests.get("https://www.fruityvice.com/api/fruit/all")
results = json.loads(fv_data.text)

#results dict to pandas dataframe
df = pd.DataFrame(results)
fv_df = pd.json_normalize(results)

#Give a fruit, get the scientific name function
a = 'Lychee'

def sci_name_getter(a):
    fruit = fv_df.loc[fv_df["name"] == a]
    print((fruit.iloc[0]['family']) , (fruit.iloc[0]['genus']))
    return

sci_name_getter(a)

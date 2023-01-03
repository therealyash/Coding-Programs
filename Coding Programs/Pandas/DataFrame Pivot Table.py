# DataFrame Pivot Table

"""
Group the data 'df' by 'month' and 'day' and find the 
mean value for columns 'rain' and 'wind' using the pivot 
table command.
"""

import io
import requests
import numpy as np
import pandas as pd

c = requests.get('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF', verify=False)
s = c.content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))
df['rain'] = df['rain'].round(6)

grp_by = df.pivot_table(index = ['month','day'],values = ['rain','wind'],aggfunc = 'mean')
print(grp_by)

#upgrad solution

import numpy as np 
import pandas as pd 
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context 
df = pd.read_csv('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF') 
df_1 = df.pivot_table(index = ['month','day'], aggfunc = 'mean') 
df_2 = df_1[['rain','wind']] 
print(df_2.head(20))

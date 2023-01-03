# DataFrame Grouping

"""
Group the dataframe 'df' by 'month' and 'day' and find the 
mean value for columns 'rain' and 'wind'.
""" 

import io
import requests
import numpy as np
import pandas as pd

c = requests.get('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF', verify=False)
s = c.content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

by = df.groupby(['month', 'day'])
df_1 = by['rain','wind'].mean()
print(df_1.head(20))
# DataFrames Merge

import pandas as pd
import numpy as np 
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context 

df_1 = pd.read_csv('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo')
df_2 = pd.read_csv('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74')
df_3 = df_1.merge(df_2, on = ['unique_id'])
print(df_3.head(20))
#DataFrame Append

import io
import requests
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

c1 = requests.get('https://query.data.world/s/vv3snq28bp0TJq2ggCdxGOghEQKPZo', verify=False)
s1 = c1.content
df_1 = pd.read_csv(io.StringIO(s1.decode('utf-8')))
c2 = requests.get('https://query.data.world/s/9wVKjNT0yiRc3YbVJaiI8a6HGl2d74', verify=False)
s2 = c2.content
df_2 = pd.read_csv(io.StringIO(s2.decode('utf-8')))

df_3 = df_1.append(df_2)
print(df_3.head())
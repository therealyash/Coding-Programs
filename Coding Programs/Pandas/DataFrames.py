# DataFrames

import io
import requests

import numpy as np
import pandas as pd
c = requests.get('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF', verify=False)
s = c.content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

print(df.describe())
print(df.columns)
print(df.shape)
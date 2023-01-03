

import io
import requests
import numpy as np
import pandas as pd

c = requests.get('https://query.data.world/s/vBDCsoHCytUSLKkLvq851k2b8JOCkF', verify=False)
s = c.content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))
df_2 = df[2::2]
print(df_2.head(20))

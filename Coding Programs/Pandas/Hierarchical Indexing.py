#Hierarchical Indexing

import pandas as pd
import numpy as np

df = pd.read_csv("rating.csv")
df['Rating'] = df.Rating.apply(lambda x: float(x))
df['Training'] = df.Rating.apply(lambda x: 'Yes' if x <= 3.5 else 'No')

# resetting and creating new index

df.reset_index(inplace = True)
df.set_index(['Office','Department'], inplace = True)
df = df.drop('index', axis = 1)
print(df.head())
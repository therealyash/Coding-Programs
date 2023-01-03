# Employee Training

import pandas as pd
import numpy as np

df = pd.read_csv("rating.csv")
df['Rating'] = df.Rating.apply(lambda x: float(x))
df['Training'] = df.Rating.apply(lambda x: 'Yes' if x <= 3.5 else 'No')
print(df.info)

"""
In the dataframe created above, find the department that 
has the most efficient team (the team with minimum percentage 
of employees who need training).
"""

# for i in ['Finance', 'HR', 'Sales', 'Marketing']:
#     print(i, len(df[(df['Training'] == 'No') & (df['Department'] == i)]) / len(df[df['Department'] == i]) * 100)


for i in ['Finance', 'HR', 'Sales', 'Marketing']:
    print(i, len(df[(df['Training'] == 'No') & (df['Department'] == i)]) / len(df[df['Department'] == i]) * 100)
import numpy as np 
import pandas as pd 
import ssl ssl._create_default_https_context = ssl._create_unverified_context 
gold = pd.DataFrame({'Country': ['USA', 'France', 'Russia'], 'Medals': [15, 13, 9]} ) 
silver = pd.DataFrame({'Country': ['USA', 'Germany', 'Russia'], 'Medals': [29, 20, 16]} ) 
bronze = pd.DataFrame({'Country': ['France', 'USA', 'UK'], 'Medals': [40, 28, 27]} )

gold.set_index('Country', inplace = True) 
silver.set_index('Country', inplace = True) 
bronze.set_index('Country', inplace = True)

total = gold.add(silver, fill_value = 0).add(bronze, fill_value = 0) 
total = total.sort_values(by = 'Medals', ascending = False) #total_1 = print(total.astype(int))
print(total.head())


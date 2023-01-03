# Loading Excel File

import pandas as pd
import numpy as np

path = "G:\\My Drive\\Study Docs\\Python\\Python Programs\\Pandas\\sales.xlsx"
sales = pd.read_excel(path,  index_col = 1)
print(sales.head())



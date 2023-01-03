# Loading csv with Index
import numpy as np
import pandas as pd

# The file is stored at the following path:
# 'https://media-doselect.s3.amazonaws.com/generic/A08MajL8qN4rq72EpVJbAP1Rw/marks_1.csv'
# Provide your answer below
csv_path = 'G:\\My Drive\\Study Docs\\Python\\Python Programs\\Pandas\\marks_1.csv'
col_names = ['S.No.','Name','Subject','Maximum Marks','Marks Obtained','Percentage']
df = pd.read_csv(csv_path,names = col_names,sep = '|',index_col = 0)


print(df)
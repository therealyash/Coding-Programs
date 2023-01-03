# Manual Indexing



import numpy as np 
import pandas as pd 
n = int(input('Enter a number: '))
num_arr = np.arange(1,n+1)
sqr_arr = num_arr * num_arr

sqr_dict = {}

for i in range(len(num_arr)):
    sqr_dict[num_arr[i]] = sqr_arr[i]

df = pd.DataFrame(sqr_dict,index = [0])
print(df)


# upGrad Solution

n = int(input())

import numpy as np 
import pandas as pd 

arr = np.arange(1, n + 1)
s = pd.Series(arr ** 2, index=arr)
print (s)



#Data Visualization
from ggplot import *
import pandas as pd

data = pd.read_csv("C:\\Users\\FAMILY\\My Jupyter Notebooks\\Udacity\\aadhaar_data.csv")

print(ggplot(data, aes('District', "Aadhaar generated")) + geom_point(color = 'coral') + geom_line(color='coral') + \
      ggtitle('title') + xlab('x-label') + ylab('y-label'))

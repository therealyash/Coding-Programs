#Udacity Practice
import pandas as pd
if True:
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print (series['Instructor'])
    print ("")
    print (series[['Instructor', 'Curriculum Manager', 'Course Number']])
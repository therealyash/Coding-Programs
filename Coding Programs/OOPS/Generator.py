import random
"""
 Generator
"""

"""
- Efficient Function that creator iterators
- use yield statement instead of return 
- speciality - it remembers last state of function and last 
  statement it had executed when yield was executed
- so when next() is called it resumes where it stopped last time
"""
"""
Example - Generator that return average of next 2 adjacent numbers in list
"""

def AvgAdj(data):
    for i in range(0,len(data)-1):
        yield (data[i] + data[i+1])/2

lst = [10,20,30,40,50,60,70]
for i in AvgAdj(lst):
    print(i)

# sample generator expressions
print(max(random.randint(10,100) for n in range(20)))

# print sum of cubes of all numbers less than 20
print(sum(n*n*n for n in range(20)))
print('**')


















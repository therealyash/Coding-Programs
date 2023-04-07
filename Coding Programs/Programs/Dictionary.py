# Dictionary
"""
Rules of Dictionary

- Dict has no indexing
- Dict is a mutable dtype
- Keys - immutable, values - mutable
- Keys should be unique

"""
# create
# empty dict
d = {}

d = {'Name':'Yash','Gender':'M'}

# access items
print(d['Name'])

# no indexing, slicing in dict

for i in d:
	print(d[i])

d2 = {'Name':'Rohit','College':'Hit','Marks':{'M1':56,'DS':54,'Eng':67}}
# accessing 2d Dict

print(d2['Marks']['DS'])

# edit a dictionary
d2['Name'] = 'Yash'
print(d2)

d2['Marks']['DS']=99
print(d2)

# get value
print(d2.get('Name'))

d2['Age'] = 23
print(d2)

# delete
del d

del d2['Age']
print(d2)

# d2.clear() will clear whole dictionary
# concat & multiply won't happen

print('Name' in d2)
print(len(d2))
print(min(d2))
print(max(d2))
sorted((d2),reverse = True)
print(d2)

# dict functions

print(d2.keys())
print(d2.values())













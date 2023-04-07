# Lists

# Array vs List
# Array are homogenous
# List can have diff datadtypes, can be heterogenous

# Array has continuous memory location
# In list it doesn't happen

# Arrays are much faster
# List are slow

# Lists are more programmer friendly

# Empty List
L = []
# Homogeneous list
L = [1,2,3,4,5]

# Heterogeneous list
L = ['Yash',1, 2,3]

# Multidimen - lists
# 2D list
L2 = [1,2,3,[4,5]]

# 3D list
L3 = [[[1,2], [3,4]], 
	 [[5,6], [7,8]]]

# type conversion
L5 = list('Yash')
print(L5)

L6 = list()

# ------

# Access 2D List
print(L2[0])
print(L2[3][0])

print(L3[1][1][0])

# Edit
# Lists are mututable
L[0] = 100
print(L)

# using slicing
L[1:4] = [200,300,400]
print(L)

# Add elements

# append-adds single element at the end of list
L.append(1000)
print(L)

# extend-adds multiple elements at the end of list

L.extend([1500,2000])
print(L)

# append adds 1 item
L.append([5,6])
# it adds it as a single item
print(L)

# extend adds multiple
L.extend('goa')
# this will add each letter of the word to the list
print(L)

# insert - adds elements at a certain position
L.insert(1,'World')
print(L)

# Delete 

# del
del L2

del L[0]
print(L)

del L[-3:]
print(L)

# remove - donno index position, but we know element
L.remove([5,6])
print(L)

# pop removes last element
L.pop()
print(L)

# Clear list - empty the list
L.clear()
print(L)

# List operations

L = [1,2,3,4]
L1 = [5,6,7,8]

print(L + L1)
print(L1 * 3)

print(4 in L)

print(len(L))
print(min(L))
print(max(L))

# Not a permanent operation
print(sorted(L))
print(sorted(L, reverse = True))

# this is permanent operation
L.sort(reverse=True)
print(L)

# index - will give index of elements
print(L.index(3))

s = "hello how are you"
lst = s.split()
new_lst = []
for i in lst:
	new_lst.append(i[0].upper() + i[1:])

s1 = " ".join(new_lst)
print(s1)

### Email id - name retrieve

s = 'yashraj@gmail.com'

name = ''
for i in s:
	if i == '@':
		index = s.index(i)
		name = s[0:index]

print('Name:',name)

# one liner for the above
print(s[:s.find('@')])

# problem 3
L1 = [1,1,2,2,3,3,4,4]
L2 = [1,2,3,4]

L = []

for i in L1:
	if i not in L:
		L.append(i)
print(L)













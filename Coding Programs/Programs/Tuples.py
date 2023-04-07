# Tuples

# Create
# Access
# Edit
# Add
# Delete
# Operations
# Functions

# Empty tuple
T1 = ()

# Homogeneous tuple
T2 = (1,2,3,4)

# Heterogeneous tuple
T3 = ('Hello',1,2,3)

# 2D tuple
T4 = (1,2,3,(4,5))

# single item tuple
T5 = (1) # not a valid way to create single item tuple
print(T5)
T5 = (1,) # use comma to create single item tuple
print(T5)

# type conversion
T6 = tuple([1,2,3,4])

# access
print(T2[0])
print(T4[-1][0])

# edit
# Tuples are immutable

# deleting tuples
del T1

# concat, add
print(T2+T3)
print(T2*3)
for i in T2:
	print(i)

# sorted function
# this returns a list not a tuple
sorted(T2)
sorted(T2, reverse = True)

# Functions

print(len(T2))
print(min(T2))
print(max(T2))
print(sum(T2))

"""
-Tuples are read only data type
-It has all read functionalities like lists
-Used where data integrity is important
"""

















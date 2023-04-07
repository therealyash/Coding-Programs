# Sets
"""
Rules of Sets

- Sets do not allow duplicates.
- Sets have no indexing so no slicing.
- Sets don't allow mutable datatypes, so no sets inside of a set, 2D or 3D set not possible.
- Set itself is a mutable datatype

"""

# Create
# dict will be formed
S1 = {}
print(type(S1))

# create empty set
S1 = set()
print(type(S1))

# homogeneous
S1 = {1,2,3,4,5}

# heterogeneous
S2 = {1,2,3,'Hello'}

# Sets don't allow duplicates
S3 = {1,2,3,1,2,3}
print(S3)

# Sets have no indexing so no slicing.
# Sets don't allow mutable datatypes, so no sets inside of a set, 2D or 3D set not possible.

S4 = {(1,2,3),'Hello'}
print(S4)
# prints hello before due to hashing in sets

# we cannot access or change sets

# add items
S1.add(6)
print(S1)

# delete items
del S2

# remove
S1.remove(1)
print(S1)

# pop
S1.pop()
print(S1)

# Set operations

S1 = {1,2,3,4}
S2 = {3,4,5,6,7}

# we can't concatenate or multiply sets

for i in S1:
	print(i)

print(1 in S1)

# Functions
print(len(S1))
print(min(S1))
print(max(S1))
print(sum(S1))

sorted(S1, reverse=True)
print(S1)

# Only set functions
print(S1.union(S2))
# common
print(S1.intersection(S2))
print(S1.difference(S2)) # item in s1 not in s2
print(S2.difference(S1)) # item in s2 not in s1
print(S1.symmetric_difference(S2)) # item not in S1, also not in S2
# disjoint means there's no common element between 2 sets
print(S1.isdisjoint(S2))
# subset means s2 contains all items of s1, also items of itself
print(S1.issubset(S2))
# 
print(S1.issuperset(S2))










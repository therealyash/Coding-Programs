# List Features

#Shallow Copying
l1 = list(range(1,6))
l2 = l1
print(l1,l2)
l2.pop()
print(l1,l2)

#Deep Copy or Cloning
l3 = list(range(1,6))
l4 = []
print(l3,l4)
l4 = l3 + l4
print(l3,l4)
l3.pop()
print(l3,l4)





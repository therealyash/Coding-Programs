
a = [1,2,34,5,6]
b = a

print(id(a))
b.append(7)
print(id(b))
print(a)
print(b)
print("---------")

c = a[::]
print(c)
c.append(6)
print(id(c))
print(a)
print(c)

print("---------")

d = a.copy()
d.append(5)
print(a,d)
print(id(a))
print(id(d))


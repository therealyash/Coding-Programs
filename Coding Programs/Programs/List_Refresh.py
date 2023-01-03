#List practice problems

L=[10,20,30,40,50,60,70,80,90,100]
#[20,40,60,80,100]
print(L[1::2])

#[20,40,60,80]
print(L[1:-1:2])

#[20,40,60,80]
x = [L[i] for i in range(1,9,2)]
print(x)

#[10,30,50,70,90]
print(L[0::2])

#[10,30,50,70]
print(L[0:-2:2])

#Add List
A = [10, 20, 30]
B = [45, 35, 25]

#returns a list of None values
x = [A.append(i) for i in B]
print(x)

B.extend(A)
print(B)

for i in A:
	B.append(i)

print(B)






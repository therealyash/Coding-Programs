# List Comprehension

L = [1,2,3,4,5,6,7]
L1 = [item *2 for item in L]
print(L1)
L3 = [i**2 for i in range(10) if i%2 != 0]

# Dictionary Comprehension

D = {'Name':'Yash', 'Gender':'Male', 'Age':30}

D1 = {key:value for key,value in D.items() if len(key) > 3}
print(D1)






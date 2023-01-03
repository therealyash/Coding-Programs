
lst = ["abc",1,2,3,4,5,6,7,8,9]
lst2 = lst.copy()
print('List: ',lst)
new_lst = []
for i in range(0,len(lst)//2):
	if i<6:
		print(i)
		new_lst.append(i)
		lst.pop(i)
new_lst.reverse()
lst = new_lst + lst
print(lst)
"""



# for i in range(0,5):
# 	l[i] = len(l) - (5+i)

# print(l)
l = ["viki",2,3,4,5,6,7,8,9,10]
x  = 5
for i in range(0,5):
	l[i] = x-i

print(l)
"""
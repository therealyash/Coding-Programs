# List Difference
# Method 1 - Element wise, element difference

list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))
total_diff = diff_list1_list2 + diff_list2_list1
total_diff.sort()
print(total_diff)

# Method 2 - Element wise, element difference

list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]

diff=[]
for x in list1:
	if not x in list2:
		diff.append(x)

for y in list2:
	if not y in list1:
		diff.append(y)

diff.sort()
print(diff)

# Method 3 - Element wise value difference

L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]
L3=[]
for  i in range(len(L2)):
    L3.append(L2[i] -L1[i])
print(L3)

# Method - 4

L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]
i = 0
while i < len(L1):
    print(L1[i] - L2[i], end=' ')
    i = i + 1

# Method - 5
print()
# using list comprehension
L1 = [10, 20, 30, 24, 18]
L2 = [8, 14, 15, 20, 10]
L3 = [L1[i] - L2[i] for i  in range(0, len(L1))]
print(L3)

# Method - 6

def list_diff(list1,list2):
    list3 = []
    for i in range(0, len(list1)):
        list3.append(list1[i] - list2[i])
    return list3

print(list_diff(L1,L2))
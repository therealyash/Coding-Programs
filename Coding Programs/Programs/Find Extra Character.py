# Find extra character
"""
s1 = input('Enter string 1: ')
s2 = input('Enter string 2: ')

for i in s2:
	for j in s1:
		if i not in s1:
			print(j)
			break

"""
# 2nd method

s1 = input()
s2 = input()


if len(s2) > len(s1):
    longer = s2
else:
    longer = s1

for i in longer:
    if s1.count(i)!=s2.count(i):
        print(i)
        break
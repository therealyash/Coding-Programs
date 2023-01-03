# Program for Split Function

s = input('Enter a string: ')
L = []
temp = ''

for i in s:
	if i != ' ':
		temp = temp + i
	else:
		L.append(temp)
		temp = ''
#L.append(temp)
print(L)



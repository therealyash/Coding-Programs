# Pallindrome Program

s = input('Enter a string: ')
flag = True
for i in range(0,len(s)//2):
	if s[i] != s[len(s) - i - 1]:
		flag = False
		print('Not a Pallindrome!')
		break
if flag:
	print('Pallindrome!')

	
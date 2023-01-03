

s = input('Enter a string: ')


def stepLetters(s):
	step = 3
	asc_val = 0
	s2 = ''
	for i in s:

		asc_val = ((ord(s[s.index(i)])) + step)
		s2 = s2 + chr(asc_val)
		

	return s2

x = stepLetters(s)
print(x)

# asc_val = ((ord(s[2])) + step)
# s2 = s2 + chr(asc_val)
# print(asc_val,s2)
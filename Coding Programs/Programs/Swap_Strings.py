# Swap upper string letters to lower and lower letters to upper
# HackerRank Solution
s = input('Enter a string: ')


def swapString(s):
	new_s = ''
	for i in s:
		if i.islower():
			new_s = new_s + i.upper()
		elif i.isupper():
			new_s = new_s + i.lower()

	return new_s

x = swapString(s)
print(x)
print(s.swapcase())

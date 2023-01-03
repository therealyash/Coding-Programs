# Calculate the Frequency of a character in a string

s = input('Enter a string: ')
char = input('Enter a char to calculate freq: ')

if len(char) > 0 and len(char) < 2:
	if char not in s:
		print('Character not in the string!')
	else:
		freq = 0
		for i in s:			
			if i == char:
				freq += 1
		print(freq)
else:
	print('Enter a single character!')
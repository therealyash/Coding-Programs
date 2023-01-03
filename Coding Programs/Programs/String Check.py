# String Check

s1 = input('Enter a string: ')





def stringCheck(s1):
	sym_lst = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
	num_lst = ['0','1','2','4','5','6','7','8','9']
	chars_lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	sym_str = ''.join(sym_lst)
	num_str = ''.join(num_lst)
	chars_str = ''.join(chars_lst)
	check = ''
	symbol_str = ''
	character_str = ''
	digit_str = ''
	float_str = ''

	for i in s1:
		if i in sym_str:
			symbol_str = symbol_str + i
		elif i in chars_str:
			character_str = character_str + i
		elif i in num_str:
			num_str = num_str + i
		elif i in num_str or i == '.':
			float_str = float_str + i


	if len(symbol_str) > 0:
		return 'STR'

	elif len(character_str) > 0:
		return 'STR'

	elif len(float_str) > 0:
		return 'FLOAT'

	elif len(num_str) > 0:
		return 'INT'

	else:
		return 'Null'


	

x = stringCheck(s1)
print(x)

"""
def stringCheck(s):
	if s.isalpha() or s.isdecimal():
		return 'STR'
	elif s.digit():
		return 'INT'

x = stringCheck(s1)
print(x)
"""

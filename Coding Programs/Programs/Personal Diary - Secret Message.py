"""
Personal Diary - Secret Message

"""
import string
from string import punctuation

# finding no. of occurence of an element in a list
def find_nth_occurrence(lst, value, n):
	indices = [index for index, item in enumerate(lst)
			   if item == value]

	if len(indices) < n:
		return -1

	return indices[n - 1]


# encoding-decoding 
def secretMessage(s,step):
	char = list(string.ascii_lowercase) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.ascii_uppercase) + [' '," ",'.']
	new_lst = []
	symb = list(punctuation)
	for i in s:

		if i in symb:
			new_lst.append(i)
			continue

		elif i == ' ':
			new_lst.append(' ')
			continue

		elif i == '.':
			new_lst.append('.')
			continue
	
		elif i in char:

			if i == 'a' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue

			if i == 'b' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue

			if i == 'c' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue

			if i == 'd' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue

			if i == 'A' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue

			if i == 'B' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue

			if i == 'C' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue

			if i == 'D' and step < 0:
				new_lst.append(char[find_nth_occurrence(char,i,2)+step])
				continue
		
			else:
				new_lst.append(char[char.index(i)+step])
					
		else:
			new_lst.append(i)
			continue
	new_str = "".join(new_lst)
	return new_str


# taking input
def messageInput():
	print('Welcome to Secret Message Diary!')
	a = int(input('Enter 1 to Encode or Enter 2 to Decode\nEnter here: '))
	s = input('Enter your message: ')
	step = int(input('Enter a step value: '))
	val = ''

	match a:
		case 1:
			val = secretMessage(s,step)
			print('Encoded Message: ',val)
		case 2:
			val = secretMessage(s,-step)
			print('Decoded Message: ',val)


messageInput()


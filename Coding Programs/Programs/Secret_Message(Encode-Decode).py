# Secret Message


# Method 1
# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# def convert_str(string, step):
#     converted = ""
#     for char in string:
#         if char != "Z":
#             converted += letters[letters.index(char) + step]
#         else:
#             converted += letters[step-1]
#     return converted

# in_str = input("string: ")
# print(convert_str(in_str, 4))

#Method 2
# import ast
# n = input()
# string = n[0]
# step = n[1]
# letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# l1='abcdefghijklmnopqrstuvwxyz'
# l2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# converted = ""
# def convert_str(string, step):
#     converted = ""
#     for char in string:
#         if char.islower():
#             converted += l1[l1.index(char) + step]
#         elif char.isupper():
#             converted += l2[l2.index(char) + step]
#         elif char != "Z":
#             converted += letters[letters.index(char) + step]
#             print(converted)
#         else:
#             converted += letters[step-1]
#     return converted
# print(convert_str(string, -step))

# Method 3
# Secret Message - Diary Msg
import string
from string import punctuation

# input
s = input('Enter a string: ')
step = int(input('Enter step value: '))

# list of all characters
char = list(string.ascii_lowercase) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.ascii_uppercase) + [' '," "]
new_lst = []
symb = list(punctuation)

def find_nth_occurrence(lst, value, n):
    indices = [index for index, item in enumerate(lst)
               if item == value]

    if len(indices) < n:
        return -1

    return indices[n - 1]

# looping in the string
for i in s:

	if i in symb:
			new_lst.append(i)
			continue

	if i == ' ':
			new_lst.append(' ')
			continue
	
	if i in char:

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
		
		else:
			new_lst.append(char[char.index(i)+step])
		

new_str = "".join(new_lst)
print('Swapped String: ',new_str)


















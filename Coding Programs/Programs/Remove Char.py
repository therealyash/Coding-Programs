# Remove a character from a string

s = input('Enter a string: ')
char = input('Enter a character to remove: ')
s_lst = [*s]
new_lst = s_lst.remove(char)

new_str = ''.join(s_lst)
print(new_str)
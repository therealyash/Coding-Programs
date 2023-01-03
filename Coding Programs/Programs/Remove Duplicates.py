#Remove Duplicates

import ast

my_list = ast.literal_eval(input('Enter list values: '))
d = {}
for item in my_list:
	if item not in d:
		d[item] = 1
	else:
		d[item] = d[item] + 1

print(list(d.keys()))
print(d)




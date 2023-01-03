# Second Maximum Number

import ast
input_str = input("Enter numbers with comma: ")
input_list = ast.literal_eval(input_str)

m = max(input_list)
second_max = float("-inf")

for i in input_list:
	if i!= m:
		if second_max < i:
			second_max = i

if second_max == float("-inf"):
	print('not present')
else:
	print(second_max)
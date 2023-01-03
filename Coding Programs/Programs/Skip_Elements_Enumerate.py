# skip elements with enumerate function

def skip_elements(list1):
	new_list = []							# initialize new list
	for index, item in enumerate(list1):	# iterating using enumerate()
		if (index % 2 == 0):
			new_list.append(item)			# adding elements to the new list

	return new_list

print(skip_elements(['a','b','c','d','e','f']))



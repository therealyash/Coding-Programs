# skip elements from the sentence

def skip_elements(sentence):

	# initialize variables
	new_list = []							# variable to add the new list
	i = 0									# variable to count the index
	
	for x in sentence:
		
		if (i % 2 == 0):					
			new_list.append(x)				# adding new elements to the new list

		i += 1								# incrementing i 

	return new_list

print(skip_elements(["Hello","how","are","you","Yashraj"]))

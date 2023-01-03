# List to Dict
names_list = ["Raj","Suresh","Ramesh","Siddhi","Priya"]
cellno_list = [9191919191,9292929292,9393939393,9494949494,9595959595]
dict1 = {}   


for name in names_list:
	for no in cellno_list:
		dict1[name] = no
		cellno_list.remove(no)
		break

print(dict1)


# Reversing a dictionary
#print(dict(reversed(list(dict1.items()))))





# def convert_to_dict(names,cellno):

# 	for names,cellno in dict1.items():
# 		for name in names:
# 			for no in cellno:
# 				print(name,no)
# 	print(dict1)

# convert_to_dict(names_list,cellno_list)




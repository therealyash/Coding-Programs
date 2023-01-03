# Function to replace the 'title()' function in python


s = input('Enter a string: ')

def title_fun(s):
	L = []
	for i in s.split():
		L.append(i[0].upper() + i[1:].lower())
	return (" ".join(L))

print(title_fun(s))



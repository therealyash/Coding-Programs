# initial letters retrieve from the string

def initials(phrase):
	words = phrase.split()
	result = ""
	for word in words:
		result = result + word[0]
	return(result.upper())

print(initials("Active Teens Taking Initiative To Understand Driving Experiences"))
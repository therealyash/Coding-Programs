# Temerature scales conversion

def to_celsius(x):					# function to convert to celcius
	return (x-32) * (5/9)

for x in range(0,101,10):			#interating a range
	print(x," ", to_celsius(x))

# with formatting

for x in range(0,101,10):			#interating a range
	print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))

# Weird Sum

#input in the form of string
n = input('Enter a number: ')

def weirdSum(n):
	sum = 0
	for i in range(1,int(n)+1):
		sum = sum + int(n*i)

	return sum

x = weirdSum(n)
print('Weird Sum: ',x)




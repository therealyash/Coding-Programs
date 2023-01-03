#Calculate Sum of Squares 

#Calculates Square 
def square(n):
	return n*n

def sum_square(x):
	sum = 0
	for i in range(x):
		sum += square(i)
	return sum

print(sum_square(10))



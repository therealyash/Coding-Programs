# Factorial Function

def factorial(n):
	result = 1
	for i in range(1,n+1):			# iterating a range from 1 to n 
		result = result*i    		# product of result and i
	return result

n = int(input("Enter a number to get factorial:- "))
print(factorial(n))
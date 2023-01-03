# Factorial Function

#take the input here
number=int(input())



#the function definition starts here
def factorial(n):

	#check if the number is greater than 0 or not
	if n > 0:
		fact = 1
		while n>0:
			if n>0:
				fact = fact*n
				n -= 1
			
		return fact

	# n is equal to 0
	elif n == 0:
		return 1

	# n is less than 0
	else:
		return -1

#do not alter the code typed below
k=factorial(number)
print(k)

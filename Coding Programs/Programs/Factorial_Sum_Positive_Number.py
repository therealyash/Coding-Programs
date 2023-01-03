# recursive function sum of numbers 

def sum_positive_numbers(n):
	#the base case is n being smaller
	if n<1:
		return 0

	#recursive case is adding this number to 
	#the sum of numbers is smaller than this one
	return n+sum_positive_numbers(n-1)

print(sum_positive_numbers(3))
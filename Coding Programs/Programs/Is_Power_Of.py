# is power of 

def is_power_of(number, base):
	# base case when number is smaller than base
	if number < base:
		#if number is equal to 1, it's a power (base**0)
		return number == 1
	result = number/base
	#recursive case : keep dividing number by base
	return is_power_of(result,base)

print(is_power_of(8,22))
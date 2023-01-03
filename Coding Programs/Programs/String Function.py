# Program to convert a integer to a string without using 'str()'

n = int(input('Enter a number: '))
digits = '0123456789'
result = ''

while n != 0:
	result = digits[n % 10] + result
	n = n // 10

print(result)
print(type(result))







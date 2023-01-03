#Armstrong Number

# Program to take input from user until the count of the number is 3
n = int(input('Enter a 3 digit number: '))
count = 0
while n != 0:
	n = n // 10
	count += 1

else:
	if count < 3:
		print('Please enter a valid 3 digit number.')
		n = int(input('Enter a 3 digit number: '))
		goto n

	elif count >= 3:
		
		print(count)


# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")


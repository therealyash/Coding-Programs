# Reverse a 4 Digit Number

number = int(input('Enter a 4 digit number: '))

# Initiate value to null
revs_number = 0

# reverse the integer number using the while loop

while (number > 0):
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10

# Display the result
print("The reverse number is : {}".format(revs_number))


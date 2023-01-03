# Calculate Sum & Average of an Unknown List with Input from User
import sys
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements: "))
print("You have entered: " + str(n))
print("Enter " + str(n) + " elements")
# iteration til the range ends
for i in range(n):
    element = int(input())
    lst.append(element)  # adding element

print(lst)

# initiating length of list and sum
sum = 0
length = 0

for x in lst:
    sum += x
    length += 1

print("Total sum: " + str(sum) + " Average is: " + str(sum / length))
print(sys.version)

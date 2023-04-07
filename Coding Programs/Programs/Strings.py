# Strings Python

# Strings are sequence of characters
# In python strings are sequence of Unicode characters


# Creatings Strings

c = 'Hello'
d = "Hello"
# Multiline Strings - ex - blog text
e = """Hello"""	
f = '''Hello'''
g = str('Hello')

# Accessing Substrings

# Indexing - single character extractions
# Type of indexing - Positive, Negative
# Positive starts from 0
c = 'Hello'
print(c[0])

# Negative starts from -1
print(c[-1])


# Slicing - multi character extraction
c = "Hello World"
print(c[0:5])
print(c[2:])
print(c[:4])
print(c[:])
print(c[2:6:2]) # last number is step, it skips
print(c[0:8:3])

# The below code won't work because
# negative indexing doesn't work
# with positive numbers
print(c[0:6:-1])

# this will give output as negative
# numbers are used
# here -1 will not be printed
print(c[-5:-1:2])

print(c[::-1])

print(c[-1:-5:-1])


# Editing & Deleting Strings
c = "Hello"

# In python strings are Immutable
#c[0] = 'X' # this will not work

# we can reassign but we cannot
# change the existing string

# Deletion
# this will delete the variable
del c

# we can't do del c[0] as well


# String Operations

# Concatenation & Multiplication
c = "Hello" + "-" + "World"
print(c)

print("Hello"*5)

# Relational Operators
"Hello" == "Hello" # will return True
"Mumbai" > "Pune" # will return False due to Lexiographically - according to the dictionary


# also cap letters come before small letters so they have higher value

# '' - empty strings are false
# 'H' - non empty strings are true

c = "Hello World"
for i in c:
	print(i)

# Membership operators
# in & not in

# String Function

# Common Functions

print(len(c))
print(max(c)) # max on ascii values
print(min(c)) # min on ascii values
print(sorted(c)) # sort on ascending values based on ascii
print(sorted(c, reverse = True))

# String Specific Functions
# Capitalize - capitalizes first letter of string
c = "hello world"
print(c.capitalize())

# Title capitalizes first letter of every word in string
print(c.title())

# Lower & Upper
print(c.lower())
print(c.upper())
print(c.swapcase())

# Count - counts the frequency of substring
print(c.count("e"))

# Find - gives index of the substring specified
# if string not present then it gives output -1
# if similar thing done in index and the string isn't present then it gives error
print(c.find("o"))

# endswith
print(c.endswith("d"))

print(c.startswith("d"))

# format
print("Hello {}! How are you?".format("Yash"))

print("Hello {}! My age is {}".format("Yash",30))

print("Hello {1}! My age is {0}".format("Yash",30))

print("Hello {name}! My age is {age}".format(name="Yash",age=30))

# Other Function

# checks if the string is alphanumeric
print("Flat20".isalnum())

# checks if the string is alphabet
print("Flat".isalpha())

# checks if string is decimal, digit

print("20".isdigit())
# space isn't identifier, '_' is valid
print("hello_world".isidentifier())


# Split Function
c = "Hello World! I live in LA"
print(c.split("I"))

# Join
print("/".join(['Hello World! ', ' live in LA']))

# Replace
print("Hi my name is Yash".replace("Yash","Omen"))

# Strip
name = "     yash is great"
print(name.strip())


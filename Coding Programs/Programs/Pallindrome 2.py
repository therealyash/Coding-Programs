
# Palindrome Program

# input from user and converting it into lower string
s = input('Enter a name: ').lower()

# program to check if the string is a pallindrome or not
def palld(s):
    if s == s[::-1]:
        return 1
    else:
        return 0

x = palld(s)
print(x)
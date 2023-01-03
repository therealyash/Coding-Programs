# Pallindrome 3

# input
s = input('Enter a name: ').lower()

def palld2(s):
    # reverse the string
    palld2.r = ''
    for i in s:
        palld2.r = i+palld2.r
    # print(r)
    # check whether the string is or not
    if palld2.r == s:
        return 1
    else:
        return 0

x = palld2(s)
print(x)
print(palld2.r)



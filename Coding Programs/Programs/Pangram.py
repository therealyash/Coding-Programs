# Pangram
# Program to check if the given string is a pangram or not

def ispangram(s):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(s.lower())

s = 'The quick brown fox jumps over the lazy dog!'
print(ispangram(s))
print(set(s.lower()))





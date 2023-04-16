# Write a python program that accepts a hyphen-separated sequence of words as input and calls a function
# convert() which converts it into a hyphen-separated sequence after sorting them alphabetically.
# For example - input - 'here-come-the-dots-followed-by-dashes'
# output - 'by-come-dashes-dots-followed-here-the


def convert(s):
    clr_str = s.split('-')
    clr_str.sort()
    return "-".join(clr_str)


s = 'here-come-the-dots-followed-by-dashes'
print(convert(s))



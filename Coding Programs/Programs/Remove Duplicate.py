"""
Write a python program that defines a function convert()
receives a string containing a sequence of whitespace separated words and returns
a string after removing all duplicate words and sorting them alphanumerically

Ex - 'Sakhi was a singer because her mother was a singer, and Sakhi\'s mother was a singer because
her father was a singer'

O/p - Sakhi Sakhi's a and because father her mother singer singer, was
"""

s = 'Sakhi was a singer because her mother was a singer, and Sakhi\'s mother was a singer because her father was a singer'

def dup_sort(s):
    s_list = s.split(' ')
    set_s = set(s_list)
    new_lst = list(set_s)
    new_lst.sort()
    return " ".join(new_lst)

print(dup_sort(s))

# It can also be done in this way

def convert(s):
    words = [word for word in s.split(' ')]
    return " ".join(sorted(list(set(words))))
print(convert(s))









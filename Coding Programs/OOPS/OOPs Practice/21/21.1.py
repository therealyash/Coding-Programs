"""
Generator
"""

"""
Write a program that proves that a list is an iterable and not an iterator
"""

lst = [10,20,30,40,50]
print(dir(lst))     # contains iter - means its iterable
i = iter(lst)
print(dir(i))       # contains iter and next - means its iterator



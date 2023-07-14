"""
Iterables vs Iterators
"""
# Making my own for loop

def yashFor(iterable):

    iterator = iter(iterable)

    while True:

        try:
            print(next(iterator))
        except StopIteration:
            break

a = [1,2,3,4,5]
yashFor(a)





















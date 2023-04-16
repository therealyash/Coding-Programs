"""
Write a function to create and return a list containing tuples of
the form (x,x^2,x^3) for all x between 1 and 20 (both included)
"""


def sqr_cube():
    sqr_cube = []
    for i in range(1, 21):
        sqr_cube.append((i,i**2,i**3))

    return sqr_cube

print(sqr_cube())





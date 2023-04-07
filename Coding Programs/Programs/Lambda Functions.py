# Lambda Functions

x = lambda x: x ** 2
x(9)

# Difference
# 1. Lambda has no return value
# 2. Can be written in 1 line
# 3. Not used for code reusabiilty
# 4. No Name

# Use Lambda Function with higher order function
# Higher order function - these function which need a function as an input, or else a function is returning another function

b = lambda x: x[0] == 'a'
print(b('apple'))

c = lambda x: "Even" if x % 2 == 0 else 'Odd'


def return_sum(func, L):
    result = 0

    for i in L:
        if func(i):
            result = result + i
    return result


L = [11, 14, 21, 23, 56, 78, 45, 29, 28]

d = lambda x: x % 2 == 0
e = lambda x: x % 2 != 0
f = lambda x: x % 3 == 0

print(return_sum(d, L))
print(return_sum(e, L))
print(return_sum(f, L))

# Map Function
# map(function, iterables)

D = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: x * 2, D)))

# Filter - works with condition
# filter(func condition, iterable)

print(list(filter(lambda x:x>3, D)))
fruits = ['Apple', 'Orange', 'Mango', 'Guava']

print(list(filter(lambda fruit: 'e' in fruit, fruits)))

# reduce
import functools

print(functools.reduce(lambda x,y: x+y, L))







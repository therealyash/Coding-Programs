# Recursion Function

# Firstly calculate base case
# Secondly make big problems into smaller modules

def mul(a, b):
    if b == 1:
        return a
    else:
        return a + mul(a, b - 1)


print(mul(5, 6))


# Factorial using recursion

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)


print(fact(5))


# Pallindrome Recursion

def palin(text):
    # len < 1 will make sure it works for even number of letters in a string
    if len(text) == 1:
        print('Pallindrome!')
    else:
        if text[0] == text[-1]:
            palin(text[1:-1])
        else:
            print('Not a Pallindrome!')


print(palin('Yash'))
print(palin('madam'))

# Fibonacci Series
# Time consuming, inefficient code
import time


def fib(m):
    if m == 0 or m == 1:
        return 1
    else:
        return fib(m - 1) + fib(m - 2)


start = time.time()
print(fib(36))
print(time.time() - start)


# Memoization - part of Dynamic Programming
# To avoid time - space - time tradeoff

def memo(m, d):
    if m in d:
        return d[m]
    else:
        d[m] = memo(m - 1, d) + memo(m - 2, d)
        return d[m]


start = time.time()
d = {0: 1, 1: 1}
print(memo(36, d))
print(time.time() - start)

# Program for Power Set
lst = [1, 2]

def power(lst):


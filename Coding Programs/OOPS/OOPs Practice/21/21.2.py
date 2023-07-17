"""
Iterator & Generator
"""

"""
Write a program that generates prime numbers below 3 million. Print sum of
these prime numbers
"""


def isPrime(n):
    # number divided by itself
    if n>1:
        if n==2:
            return True
        if n%2 == 0:
            return False
        for i in range(2, n//2):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False


def generatePrimes():
    n = 1
    while True:
        if isPrime(n):
            yield n
        n += 1

total = 0
for next_prime in generatePrimes():
    if next_prime <




gen = (i for i in range(3000000))

print(sum(gen))



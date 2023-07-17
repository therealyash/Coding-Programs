"""
Check Prime
"""

n = int(input('Enter a number to check if it is prime: '))

def checkPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True

print(checkPrime(n))

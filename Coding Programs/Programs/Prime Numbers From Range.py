# Prime Numbers from Range
# Algorithm
"""
1. Define a function that takes two arguments: start and end.
2. Create an empty list called "primes" to hold the prime numbers.
3. Loop over each number in the range [start, end].
4. For each number, check if it is greater than 1.
5. If the number is greater than 1, loop over each
   integer i in the range [2, sqrt(num) + 1].
6. For each i, check if num is divisible by i.
7. If num is divisible by i, break out of the loop.
8. If num is not divisible by any i, append num to the "primes" list.
9. Return the "primes" list.
"""

import math

def generate_primes(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(math.sqrt(num))+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

start = 10
end = 50

primes = generate_primes(start, end)
print(primes)



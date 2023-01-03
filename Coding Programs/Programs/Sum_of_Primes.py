#Sum of Primes

n = int(input("Enter a number: "))
list = []
sum = 0
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
           break
    else:
        sum = sum + i
print("Sum of primes from 2 to {0} is {1}".format(n,sum))
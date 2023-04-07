# First 10 Prime Numbers

# returns the next prime number
def next_prime(num):
    num += 1
    while True:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            return num


# generates n prime numbers
def prime_producer(n):
    num, count = 1, 1
    while count <= n:
        num = next_prime(num)
        yield num
        count += 1


n = int(input('How many prime numbers you want to generate? '))
# create a list to add number
l = [x for x in prime_producer(n)]

print(l)
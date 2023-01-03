# Sum of prime from 2 to n

n = int(input('Enter a number: '))
sum = 0

for i in range(2,n+1):
	for j in range(2,i):
		if i % 2 == 0:
			break
		else:
			sum += i

print(sum)
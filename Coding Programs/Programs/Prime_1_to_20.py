# Print prime numbers from the range 1 to 20

for n in range(1,20):
	flag = True
	for i in range(2,n):
		if n % i == 0:
			flag = False
			break
	if flag:
		print(n)
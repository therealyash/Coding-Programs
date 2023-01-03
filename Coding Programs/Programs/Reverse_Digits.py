# Reverse Digits

n = int(input("Enter a Number to Reverse: "))
rev = 0
while n>0:
	if n > 0:
		rev = (rev * 10) + (n % 10) 
		n = n // 10
print(rev)
	
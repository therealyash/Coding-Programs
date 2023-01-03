

n = int(input('Enter a number: '))
res = ''
digits = '0123456789'
while n != 0:
    print(res)
    res = digits[n%10] + res
    n = n // 10

print(res)






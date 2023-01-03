#3n

# 3n+1 - beautiful, 3n+2 - pretty, 3n - sexy

k = int(input("Enter a number: "))

b,p,s = [],[],[]
for i in range(1,21):
   b.append(3*i+1)
   p.append(3*i+2)
   s.append(3*i)

if k % 3 == 0:
   print('Sexy')
elif k % 3 == 1:
   print('Beautiful')
elif k % 3 == 2:
   print('Pretty')

# print(b)
# print(p)
# print(s)
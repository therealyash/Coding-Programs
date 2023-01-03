# Fenced Matrix (Boundaries covered with 1)
import ast

mylist = ast.literal_eval(input('Enter numbers with comma: '))
m = mylist[0]
n = mylist[1]

# will create [0,0,0,0,] list
final = [0]*n

final = [list(final) for i in range(m)]

#printing matrix with 0 numbers
for i in final:
	print(i)

print()

for i in range(m):
	for j in range(n):
		if i==0 or j==0 or i==m-1 or j==n-1:
			final[i][j] = 1

for i in final:
	print(i)


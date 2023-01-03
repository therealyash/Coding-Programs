# Practicing Nested For loops

# # square box stars
# for i in range(5):			# iterating number of rows
# 	for j in range(5):		# iterating number of stars printing
# 		print('*', end=' ')
# 	print()					# continue the next loop output on next line

# # increasing triangle pattern
# for i in range(5):
# 	for j in range(i+1):
# 		print('*', end=' ')
# 	print()

# decreasing triangle pattern

# for i in range(n):
# 	for j in range(n-i):
# 		print('*', end =' ')
# 	print()

# # alternate option for decreasing triangle pattern

# for i in range(n):
# 	for j in range(i,n):
# 		print('*', end = ' ')
# 	print()

# right angled triangle pattern
# n = 5
# for i in range(n):
	
# 	for j in range(i,n):
# 		print('', end = ' ')

# 	for k in range(i+1):
# 		print('*', end = '')

# 	print()

# right angled triangle pattern 2

# for i in range(n):

# 	for j in range(i+1):
# 		print('', end = ' ')

# 	for k in range(i,n):
# 		print('*', end = '')

# 	print()

# triangle hill pattern

# for i in range(n):

# 	for j in range(i,n):
# 		print('', end =' ')

# 	for k in range(i):
# 		print('*', end = '')

# 	for l in range(i+1):
# 		print('*', end = '')

# 	print()

# # inverted triangle hill pattern

# n = 5
# for i in range(n):			# iterating number of rows

# 	for j in range(i+1):
# 		print('', end = ' ')

# 	for j in range(i,n-1):
# 		print('*', end = '')

# 	for k in range(i,n):
# 		print('*', end = '')

# 	print()

# diamond pattern hill pattern + inverted hill pattern

# for i in range(n-1):

# 	for j in range(i,n):
# 		print(' ', end ='')

# 	for k in range(i):
# 		print('*', end = '')

# 	for l in range(i+1):
# 		print('*', end = '')

# 	print()


# for i in range(n):			# iterating number of rows

# 	for j in range(i+1):
# 		print('', end = ' ')

# 	for j in range(i,n-1):
# 		print('*', end = '')

# 	for k in range(i,n):
# 		print('*', end = '')

# 	print()


# square bar pattern

# n = 5
# for i in range(n):

# 	for j in range(n):
# 		if (j == 0) or (j == n-1):
# 			print('*', end =' ')
# 		else:
# 			print(' ', end = '')
# 	print()


# plus pattern
# n = 5
# for i in range(n):

# 	for j in range(n):
# 		if(j == 2) or (i==2):			# alternatively can be done as if(n//2) or (j//2)
# 			print('*', end = ' ')
# 		else:
# 			print(' ', end = ' ')
# 	print()



# cross pattern or diagonal pattern

# n = 5
# for i in range(n):
# 	for j in range(n):
# 		if (i==j) or (i+j == n-1):
# 			print('*', end = ' ')
# 		else:
# 			print(' ', end = ' ')

# 	print()

# hollow square pattern
# n = 5
# for i in range(n):
# 	for j in range(n):
# 		if (i==0) or (j==0) or (i==n-1) or (j==n-1):
# 			print('*', end = ' ')
# 		else:
# 			print(' ', end =' ')

# 	print()

# hollow increasing triangle

# for i in range(n):
# 	for j in range(i+1):
# 		if(i==n-1) or (i==j) or (j==0):
# 			print('*', end=' ')
# 		else:
# 			print(' ', end =' ')

# 	print()

# hollow decreasing triangle
# for i in range(n):
# 	for j in range(i,n):
# 		if (j==n-1) or (i==0) or (j==i):
# 			print('*', end =' ')
# 		else:
# 			print(' ', end =' ')

# 	print()

# hollow hill pattern

# for i in range(n):

# 	for j in range(i,n):
# 		print(' ', end =' ')

# 	for k in range(i):
# 		if (i==n-1) or (k==0):
# 			print('*', end =' ')
# 		else:
# 			print(' ', end =' ')

# 	for l in range(i+1):
# 		if (i==n-1) or (l==i):
# 			print('*', end =' ')
# 		else:
# 			print(' ', end =' ')
# 	print()


# hollow diamond pattern
n = 5
for i in range(n-1):				# hill
	for j in range(i,n-1):
		print(' ', end =' ')

	for j in range(i):
		if j==0:
			print('*', end =' ')
		else:
			print(' ', end =' ')

	for j in range(i+1):
		if j==i:
			print('*', end =' ')
		else:
			print(' ', end =' ')
	print()

for i in range(n):				# inverted hill
	for j in range(i):
		print(' ', end =' ')

	for j in range(i,n):
		if j==i:
			print('*', end =' ')
		else:
			print(' ', end =' ')

	for j in range(i,n-1):
		if j==n-2:
			print('*', end =' ')
		else:
			print(' ', end =' ')
	print()					























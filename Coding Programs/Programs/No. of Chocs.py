# Number of Chocolates

#input
input_str = input('Enter 2 numbers: ')
x = input_str.split(',')
y = list(map(lambda x:int(x),x))

money,choc_cost = y


choc = money // choc_cost
wrap = money // choc_cost

while wrap // 3 != 0:
	choc = choc + wrap // 3
	wrap = wrap // 3 + wrap % 3

else:
	print(choc)


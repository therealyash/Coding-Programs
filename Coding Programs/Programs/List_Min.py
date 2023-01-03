#List Min

#smallest in a list
#1st minimum
lst = [-2,3,0,7,2,1]


def min_lst(lst):
	min_lst.m = lst[0]
	for i in lst:
		if i<min_lst.m:
			min_lst.m = i
	ind = lst.index(min_lst.m)
	return print('Minimum: ',min_lst.m)


min_lst(lst)
lst.remove(min_lst.m)
min_lst(lst)










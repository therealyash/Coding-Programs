#Map, Filter, Reduce

# Map Function - used to perform ops on multiple entities

#using lambda
list_numbers = (1,2,3,4) 
sample_map = map(lambda x: x*2, list_numbers) 
print(list(sample_map))

#using user-defined
def multi(x): 
	return x*2 

list_numbers = [1,2,3,4] 
sample_map = map(multi, list_numbers) 
print(list(sample_map))

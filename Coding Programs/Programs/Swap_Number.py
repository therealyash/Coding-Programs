# Swap Numbers and take input from string

input_str = "20,50"
upd_str = input_str.replace(',',' ')
print(upd_str)
lst = upd_str.split()
num_lst = list(map(lambda x:int(x),lst))
print(num_lst)
a,b = num_lst
print(f"Numbers a = {a},b = {b}".format(a,b))
c = a; a = b; b = c;
print(f"Numbers after replacing a = {a},b = {b}".format(a,b))



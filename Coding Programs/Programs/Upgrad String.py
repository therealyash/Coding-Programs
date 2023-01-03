# upGrad String

upgrad_str = input('Enter a string: ')
dict1 = {}

for key in upgrad_str:
    if key not in dict1:
        dict1[key] = 1 
    else:
        dict1[key] += 1 

dict2 = {k:v for k, v in sorted(dict1.items(),key=lambda x: x[1])}
to_check = list(dict2.values())

if to_check == list(range(1,len(dict1)+1)):
    print(True)
else:
    print(False)
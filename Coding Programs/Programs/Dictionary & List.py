#Dictionary & List

#input has been taken for you
import ast
#input_str = input()
#input dictionary has been received in input_dict
input_dict = {'Mobile':['Redmi','Samsung','Realme'],'Laptop':['Dell','HP'],'TV':['Videocon','Sony']}	#ast.literal_eval(input_str)
# lst = []

# start writing your code here
# x = 0
# for i in input_dict.keys():
# 	for j in input_dict.values():
# 		lst.append(str(i)+''+str(j))
		

#print(lst)

def mapStrings(item):
    key, value_list = item[0], item[1]  
    result = []
    for val in value_list:
        result.append(key+"_"+val)
    return result

result_list = []
for item in input_dict.items():
    result_list.extend(mapStrings(item))

print(result_list)


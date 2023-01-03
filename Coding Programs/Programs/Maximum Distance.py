#Maximum Distance

#input has been taken for you
import ast
input_list= ast.literal_eval(input())

def maxDistance(mylist, n):       
    mp = {} 

    maxDict = 0
    for i in range(n): 
        if mylist[i] not in mp.keys(): 
            mp[mylist[i]] = i   
        else: 
            maxDict = max(maxDict, i-mp[mylist[i]]) 
    return maxDict 


n = len(input_list) 
print(maxDistance(input_list, n))
#Pandas Iterrows() Method

# 


#Iter
d ={
  "fantasy": "harrypotter",
  "romance": "me before you",
  "fiction": "divergent"
  }
 
print("d.items() in (v3.6.2) = ")
for i in d.items():
 
    # prints the items
    print(i)
 
print("\nd.iteritems() in (v3.6.2)=")
 
for i in d.iteritems():
 
    # prints the items
    print(i)
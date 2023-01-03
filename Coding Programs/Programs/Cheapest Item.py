# Cheapest Item

# using min
item_list = {'A':12000, 'B':11000, 'C':13000}

cheapest = min(item_list, key=item_list.get)
value = str(item_list[cheapest])
print('{0}: {1}'.format(cheapest, item_list[cheapest]))

# using key value
item_list = {'A':12000, 'B':11000, 'C':13000}
cheapest_item=list(item_list.keys())[0]

for key in item_list.keys():
    if item_list[key]<item_list[cheapest_item]:
        cheapest_item=key 

print('{0}: {1}'.format(cheapest_item, item_list[cheapest_item]))



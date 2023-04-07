# break, continue and pass

# break used for linear searching
# break will terminate the loop
for i in range(1,11):
    if i == 5:
        break
    print(i)

print('---')

# continue will skip the code block 
# or condtion where it's present 
# continue example - showing products
# which are in stock and skipping products 
# out of stock
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# pass statement - just a filler
for i in range(1,11):
    pass



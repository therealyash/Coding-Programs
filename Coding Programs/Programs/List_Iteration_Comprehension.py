# List iteration & comprehension

L1 = ["Automobile","Honda","Suzuki","Benz"]
L2 = [len(i) for i in L1] 
print(L2)

# Iterating over 2 lists simultaneously

for i,j in zip(L1,L2):
	print(i,"-",j)

# Another similar program of Dictionary Comprehension

L1 = ["Automobile","Honda","Suzuki","Benz"]
L2 = {i : len(i) for i in L1} 
print(L2)

# Set Comprehension program

words = input("Enter a word: ")
vowels = {i for i in words if i in "aeiou"}
print(vowels)
# Tabular form representation of data


# Define the dictionary
dict1 = {}
 
# Insert data into dictionary
dict1 = {1: ["Samuel", 21, 'Data Structures'],
         2: ["Richie", 20, 'Machine Learning'],
         3: ["Lauren", 21, 'OOPS with java'],
         }
 
# Print the names of the columns.
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
 
# print each data item.
for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course))
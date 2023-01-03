# Joining 2 lists using map function


first_name = ['Ankur', 'Avik', 'Kiran', 'Nitin']
last_name = ['Narang', 'Sarkar', 'R', 'Sareen']
data = [first_name,last_name]
name = list(map(' '.join, zip(*data)))

print(name)
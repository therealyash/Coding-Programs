# miles to km

def convert_distance(miles):
	km = miles * 1.6 
	result = "{miles} miles equals {km} km".format(miles=miles,km=km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
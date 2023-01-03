def format_address(address_string):
  # Declare variables
  house_number = 0
  street_name = ""

  # Separate the address string into parts
  address_list = address_string.split()



  # Traverse through the address parts
  for i in address_list:

    if str(i).isnumeric():
        house_number = i
    # Determine if the address part is the
    # house number or part of the street name

    elif str(i).isalpha() or str(i).isalnum():
        street_name = street_name + " " + i



  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
  return "house number {} on street named {}".format(house_number,street_name)

print(format_address("123 Main Street"))
#Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

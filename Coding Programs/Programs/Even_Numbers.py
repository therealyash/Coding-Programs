# Even Numbers function

def even_numbers(maximum):
    return_string = ""
    for x in range(1,maximum+1):
        if x%2==0:
            return_string += str(x) + " "
    return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed
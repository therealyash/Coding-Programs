# Change file name extension from the element of old list to a  new list

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
old_extension = "hpp"
new_extension = "h"


for x in filenames:
    if "."+"hpp" in x:
        index = x.index("." + "hpp")
        new_name = x[0:index] + "." + new_extension
        newfilenames.append(new_name)
        
    else:
        newfilenames.append(x)
        
        

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
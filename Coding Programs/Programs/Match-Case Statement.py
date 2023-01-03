# Match-Case Statement

# First, ask the player about their CPU
cpuModel = str.lower(input("Please enter your CPU model: "))
 
# The match statement evaluates the variable's value
match cpuModel:
	case "celeron": # We test for different values and print different messages
		print ("Forget about it and play Minesweeper instead...")
	case "core i3":
		print ("Good luck with that ;)")
	case "core i5":
		print ("Yeah, you should be fine.")
	case "core i7":
		print ("Have fun!")
	case "core i9":
		print ("Our team designed nice loading screens… Too bad you won't see them...")
	case _: # the underscore character is used as a catch-all.
		print ("Is that even a thing?")
#Program to create a function to convert secondst to hrs,minutes

def convert_to_seconds(seconds):
	hours = seconds // 3600
	minutes = (seconds - hours*3600 ) // 60 #Subracting hours to avoid duplication
	remaining_seconds = seconds - (hours * 3600) - (minutes*60)
	return hours,minutes,remaining_seconds

hours,minutes,seconds = convert_to_seconds(10)
print(hours,minutes,seconds)

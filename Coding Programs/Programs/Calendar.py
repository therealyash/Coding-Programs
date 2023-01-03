# Calendar

events_list = [ [29,31], [23,26], [24,25] ]
wedding = 24

# initializing clash 0
clash = 0
for event in events_list:
	if event[0] <= wedding and event[1] >= wedding:
		clash += 1

print(clash)

input_list = [3, True]
day_of_the_week = input_list[0] #first element is an integer denoting the day of the week
is_on_vacation = input_list[1]

weekday = [1,2,3,4,5]
weekend = [6,7]
if is_on_vacation == True:
    if day_of_the_week in weekend:
        print('off')
    elif day_of_the_week in weekday:
        print('10:00')
elif is_on_vacation == False:
    if day_of_the_week in weekday:
        print('07:00')
    elif day_of_the_week in weekend:
        print('10:00')

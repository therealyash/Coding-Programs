# Team and Applicant

# Sample input:
# [23,45,34,76]
# [70,34,94]

#input
a = input('Enter team numbers with comma: ').split(',')
b = input('Enter appicant numbers with comma: ').split(',')
team = [int(i) for i in a]
applic = [int(i) for i in b]
# print(team)
team_avg = sum(team)/len(team)
# print(team_avg)
hired_lst = []
for i in applic:
	if i > team_avg:
		hired_lst.append(i)

print(hired_lst)

#worked code in upgrad platform

import ast

team = ast.literal_eval(input())
applicants = ast.literal_eval(input())

def check_above_avg(data, check):
    avg = sum(data)/len(data)
    if check > avg:
        return 1
    else:
        return 0

for a in applicants:
    is_add = check_above_avg(team,a)
    if is_add == 1:
        team.append(a)
print(team)

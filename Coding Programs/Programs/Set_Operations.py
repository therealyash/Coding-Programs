input_list = [[2, 5, 9, 12, 13, 15, 16, 17, 18, 19],
[2, 4, 5, 6, 7, 9, 13, 16],
[1, 2, 5, 9, 10, 11, 12, 13, 15]] 

C = input_list[0]
F = input_list[1]
H = input_list[2]

set_C = set(C)
set_F = set(F)
set_H = set(H)
set_all = set([x for x in range(1,21)])

# Students who play all the three sports : We can just take intersection 
# of all 3 sets to give us the answer.

all_three_sports = set_C.intersection(set_F,set_H)

# Students who play both cricket and football but don’t play 
# hockey : We can take the intersection of the set of players 
# who play football and the set of players who play cricket and 
# then subtract the set of players that play hockey.

c_and_f_but_not_h = (set_F.intersection(set_C)).difference(set_H)
# Students who play exactly two of the sports : For this, 
# we take the intersection of the set of players who play 
# football and hockey and then subtract the set of players 
# that play cricket. Secondly, we take the intersection of 
# set of players who play cricket and hockey and then subtract 
# the set of players that play football. Lastly, we take the 
# intersection of set of players who play football and cricket 
# and then subtract the set of players who play hockey.

# As we can see, this leaves us with three sets of players that 
# only play two sports. We get our answer by union-ing all the results.

only_two_sports = (set_C.intersection(set_F)-set_H).union((set_H.intersection(set_F)-set_C),(set_C.intersection(set_H)-set_F))
# Students who don’t play any of the three sports : Here we just 
# subtract the union of all the sets of players we received with 
# the total set of players.

neither_sports = set_all - (set_C.union(set_F,set_H))
# Now, we just convert set to list and sort them before printing :

print("All 3 Sports",sorted(list(all_three_sports)))
print("Cricket & Footbal but not Hockey",sorted(list(c_and_f_but_not_h)))
print("Only 2 Sports",sorted(list(only_two_sports)))
print("Neither Sports",sorted(list(neither_sports)))
# Earlier, you solved the chocolate problem where Sanjay had m rupees, 
# and the cost of each chocolate was c rupees. The shopkeeper gave 
# away one chocolate for three wrappers. In this problem, let's 
# generalise the question by saying, Sanjay has m rupees, each chocolate 
# costs c rupees, the shopkeeper will give away k chocolates for w 
# wrappers. Can you find now how many chocolates Sanjay will be a
# ble to eat?

# Input: 4 integers separated by space in order m c w k
# integers c and w will be >0
# integers m and k will be >=0
# integer k will be <w

# Output: An integer denoting the number of chocolates Sanjay will be able to get.


number = input()
myList = number.split(',')
m = int(myList[0])
c = int(myList[1])
k= int(myList[3])
w = m//c
chocolate = m//c
#start writing your code here
while w//3 !=0 :
    wrapper = (w//3)*k
    chocolate = chocolate + wrapper
    w= wrapper +w%3
print(chocolate)
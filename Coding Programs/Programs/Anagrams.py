# Anagrams

s1 = input('Enter 1st string: ').lower()
s2 = input('Enter 2nd string: ').lower()

#my code
"""
def Anagrams(s1,s2):

    for i,j in zip(s1,s2):
        if len(s1) == len(s2):
            if i in s2 and j in s1:
                return True
            else:
                return False
        elif s1.count(i) != s2.count(i):
            return False
        else:
            return False
"""
def Anagram2(s1,s2):
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1.count(s1[i]) != s2.count(s2[i]):
            return False
    else:
        return True

x2 = Anagram2(s1,s2)

# x = Anagrams(s1,s2)
print(x2)


"""

Sample Solution

#take input here
s1 = input()
s2 = input()

#code here to check if they are anagrams or no

def anagram(s1,s2):
    #if length doesnt match then they are definitely not anagrams
    if len(s1)!=len(s2):
        return False

    #we will check count of each character one by one
    for i in range(len(s1)):
        if s1.count(s1[i]) != s2.count(s1[i]):
            return False
   #if we come out of the for loop means we didnt exit the function in loop
   #remember we exit the function when we return
   #this means there was no occurance where s1.count(s1[i]) != s2.count(s1[i]) was True
   #this means the strings are anagrams
    return True

print(anagram(s1,s2))

"""


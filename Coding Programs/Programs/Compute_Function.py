#Compute Function

import math
def compute(n) :
        sum = 0
        num = 0
        for outer in range(0, n) :
                num = num * 10 + n
                sum = sum + num
        return(sum)

n = int(input())
total = compute(n)
print('The value of n + nn + nnn + nnnn is ',total)
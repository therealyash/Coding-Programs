"""
Write a program that defines a function compute() that calculates
the value of n + nn + nnn, where n is digit received by the function. Test for 4 & 7
"""


def compute(n):
    add = 0
    for i in range(1, n):
        add += int(str(n) * i)
    return add

print(compute(4))










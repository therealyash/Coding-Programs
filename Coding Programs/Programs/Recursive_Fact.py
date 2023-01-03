#Recursive Fact

def fact(n):
    if n==1:
        return n
    elif n<0:
        return "Invalid No."
    else:
        return n*fact(n-1)


a = fact(6)
print("Factorial of number is :",a)
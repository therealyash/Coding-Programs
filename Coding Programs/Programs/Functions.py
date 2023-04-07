# # Functions
# import is_Even as ev
# num = int(input('Enter a number: '))
#
# print(ev.is_Even(num))
# print(ev.is_Even.__doc__)
#
# # parameter & arguments
# # ex - while playing games, difficulty is a parameter & easy, medium, hard are arguments
#
# # 4 Arguments in Python
# # 1. Default Arguments
#
# # Default argument function
# # when we give parameters a default argument
# def power(a=1,b=1):
#     return a**b
#
# print(power(2,3))
# print(power(3))
#
# # Positional Arguments - takes arguments in an ordered fashion
# print(power(2,3))
#
# # Keyword Argument - overrides positional argument, unordered fashion
# # explictly
# print(power(b=2, a=3))
#
# # Arbitrary Argument
#
# def flexi(*number):
#     print(number)
#     product = 1
#     for i in number:
#         product = product * i
#     print(product)
#
# flexi(1,2,3)

# Global & Local Variable

def func_a():
    print('Inside func_a')

def func_b(y):
    print('Inside func_b')
    return y

print(func_a())
print(5+func_b(2))






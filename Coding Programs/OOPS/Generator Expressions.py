# Generator Expressions
import sys
lst = [i * i for i in range(15)]
gen = (i * i for i in range(15))
print(lst)
print(gen)
print(sys.getsizeof(lst))
print(sys.getsizeof(gen))
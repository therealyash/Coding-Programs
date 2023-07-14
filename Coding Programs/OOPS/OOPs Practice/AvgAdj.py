
class AvjAdj:

    def __init__(self,data):
        self.__data = data
        self.__len = len(data)
        self.__first = 0
        self.__sec = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.__sec == self.__len:
            raise StopIteration         # raises exception (runtime error)
        self.__avg = (self.__data[self.__first] + self.__data[self.__sec]) / 2

        self.__first += 1
        self.__sec += 1
        return self.__avg

lst = [10,20,30,40,50,60,70]
coll = AvjAdj(lst)
for val in coll:
    print(val)





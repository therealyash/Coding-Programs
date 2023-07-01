# Used when 2 classes have a 'has a' relationship
# 'has a' means for example a College has Professors. So College Class's object contain one or more Porfessor Class Objects
# A container can contain one or more contained objects apart from other data

class Department:

    def set_department(self):
        self.__id = input('Enter department id: ')
        self.__name = input('Enter department name: ')

    def display_department(self):
        print('Department ID is: ', self.__id)
        print('Department Name is: ', self.__name)

class Employee:
    def set_employee(self):
        self.__eid = input('Enter employee ID: ')
        self.__ename = input('Enter employee Name: ')
        self.__dobj = Department()
        self.__dobj.set_department()

    def display_employee(self):
        print('Employee ID:', self.__eid)
        print('Employee Name:', self.__ename)
        self.__dobj.display_department()

obj = Employee()
obj.set_employee()
obj.display_employee()







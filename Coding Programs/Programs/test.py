#test

class Animals():

	def __init__(self,name,color,anim_type):
		self.name = name
		self.color = color
		self.anim_type = anim_type

	def display(self):
		print("Name: ",self.name)
		print("Color: ",self.color)
		print("Animal Type: ",self.anim_type)

	def about_class(self,classname):
		print(dir(classname))

	def about_object(self,obj_name):
		print(help(obj_name))

	

#Obj1 = Animals('Lion','Ochre','Carnivores')
#Obj1.display()
#Obj1.about_class(Animals)


class Maths():
	__a = 5
	__lst = []
	# def __init__(self,a,b):

	# 				#global variables declared which can accessed anywhere in the class
	# 	#__a = 5
	# 	# b = 5
	# 	# global tup
	# 	# global dic
	# 	# global set1
	# 	# tup = () 				#empty tuple
	# 	# __lst = [] 				#empty list
	# 	# dic = {} 				#empty dictionary
	# 	# set1 = set() 			#empty set

	# 	self.a = a
	# 	self.b = b

	# 	# print("Addition: ",a+b)
	# 	# __lst.append(a+b)
	# 	# print("Subtraction: ",a-b)
	# 	# __lst.append(a-b)
	# 	# print("Multiply: ",a*b)
	# 	# __lst.append(a*b)
	# 	# print("Divide: ",a/b)
	# 	# __lst.append(a/b)
	# 	# print("Inside Init",__lst)

	def calc(self,a,b):

		self.a = a
		self.b = b
		# lst = []

		
		self.__lst.append(a+b)
		self.__lst.append(a-b)
		self.__lst.append(a*b)
		self.__lst.append(a/b)
		print("Inside Calc",self.__lst)


	def display(self):
		print(self.__a)
		print("Inside Display",self.__lst)

		x=1
		for i in self.__lst:
			print("[",x,"-",i,"]")

			x+=1

	def func(self,a,b):
		self.a = a
		self.b = b
		lst = []
		lst.append(a+b)
		print(lst)
		return lst

	def __del__(self):
		print("Destructor Called")
		




# m1 = Maths(10,5)
# m1.calc(10,5)
# m1.display()
m2 = Maths()
maths_obj = m2.func(15,10)
print(maths_obj)
m2.calc(15,10)
print(maths_obj)
#print(m2.__lst)

# Syntax for enabling private identifiers outside the class :)

#print(m2._Maths__lst)

#print(lst)
#Obj1.about_object(Obj1)
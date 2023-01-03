#Functional Arguments Example
#i,j are positonal args
#*args holds tuple
#x,y are keyword args (can be specified in any order)
#kwargs holds dictionary
def fun_args(i,j,*args,x,y,**kwargs):
	print()
	print(i,j,end ='')
	for var in args:
		print(var,end='')
	print(x,y,end = '')
	for name,value in kwargs.items():
		print(name,value,end='')

fun_args(10,20,x=20,y=40)
fun_args(10,20,100,200,x=30,y=40)
fun_args(10,20,100,200,x=30,y=40,a=5,b=6,c=7)
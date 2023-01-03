# Interactive Calc - Viki

class FormulaError(Exception):
    pass


def checkElements(lenoflist):
    if lenoflist !=3:
        raise FormulaError("Entered formula should be of 3 elements\n"
                           "a number, an operator and another number")

def checkOperator(operator):
    op_list = ["+","-","*","/"]
    if operator not in op_list:
        raise FormulaError("2nd element should be an operator\n"
                           "e.g. '+' or '-' or '*' or '/'")

def arithmatic(ele1,ele2,operator):
  if operator == "+":
    return  ele1+ele2
  if operator == "-":
    return  ele1-ele2
  if operator == "*":
    return  ele1*ele2
  if operator == "/":
    return  ele1/ele2
        
tocontinue = True
while tocontinue:
    
    try:
        print("\n---CALCULATOR---\n")
        #take a user input
        calc_input = input("Enter a formula that consist of a number, an operator and another number, seperated by white spaces. e.g. 1 + 1\n"
                           "Enter : ")
        #split the user input
        input_list = calc_input.split(" ")
        #check if it has 3 elements
        lenoflist = len(input_list)
        checkElements(lenoflist)
        #check if 2nd element is operator
        operator = input_list[1]
        checkOperator(operator)
        #check for ValueError
        ele1 = float(input_list[0])
        ele2 = float(input_list[2])
        
    except FormulaError as msg:
        print(msg)
        
    except ValueError:
        print("1st element and 2nd element should be an number(int/float)")

    else:
        #if no error found then calculate
        x = arithmatic(ele1,ele2,operator)
        print("Result : ",x,"\n")

    ans = input("Press ENTER to continue\nType QUIT to exit : ").lower()
    if ans == "quit":
        break
    else:
        pass
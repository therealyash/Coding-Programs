# Balanced Brackets (Stack Problem)

#take input
inp=input()

stack = []

for i in inp:
    if len(stack) == 0:
        stack.append(i)
    else:
        if i==')' and stack[-1]=='(':
            stack.pop()
        elif i=='}' and stack[-1]=='{':
            stack.pop()
        elif i==']' and stack[-1]=='[':
            stack.pop()
        else:
            stack.append(i)

if stack:
    print('No')
else:
    print('Yes')
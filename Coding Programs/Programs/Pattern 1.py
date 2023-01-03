# Pattern 1

# Sample Output : 

# --------e-------- 
# ------e-d-e------ 
# ----e-d-c-d-e---- 
# --e-d-c-b-c-d-e-- 
# e-d-c-b-a-b-c-d-e 
# --e-d-c-b-c-d-e-- 
# ----e-d-c-d-e---- 
# ------e-d-e------ 
# --------e-------- 

import string

n = int(input('Enter a number: '))
a = string.ascii_lowercase

List = []

for i in range(n):
    s = "-".join(a[i:n])
    List.append(s[::-1]+s[1:])
width = len(List[0])

for i in range(n-1, 0, -1):
    print(List[i].center(width, "-"))

for i in range(n):
    print(List[i].center(width, "-"))
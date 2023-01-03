# change domain program

# Program to take input from user as a any mail and change its domain

def replace_domain(email,old_domain, new_domain):
    if "@" + "hotmail.com" in email:
        index = email.index("@" + old_domain)
        new_email = email[0:index] + "@" + new_domain
        return print(new_email)
    

    elif "@" + "outlook.com" in email:
        index = email.index("@" + old_domain)
        new_email = email[0:index] + "@" + new_domain
        return print(new_email)
    

    else:
        return print(email)


email = "yash10@outlook.com"
old_domain = "hotmail.com"
new_domain = "gmail.com"


replace_domain(email,old_domain,new_domain)
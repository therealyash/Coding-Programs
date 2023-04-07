# Literal - raw data given to variable
"""
Types of Literal

- Numeric
- String
- Boolean
- Special
"""

# Numerical Literal
a = 0b1010 # binary literal
b = 100 # decimal literal
c = 0o310 # octal literal
d = 0x12c # hexadecimal literal


# float literal
f1 = 10.5
f2 = 1.5e2
f3 = 1.5e-3

# complex literal
x = 3.14j
print(x,x.imag,x.real)


# String literal
s1 = 'string'
s2 = "string"
char = "C"
multiline_str = """Multiline String"""
# unicode like smileys
unicode_ = u"\0001f600"
raw_str = r"raw \n string"

# Boolean Literal
# python wil implicitly convert to int below
a = True + 4


# Special Literal
# none means absense of anything
# We can't declare variables in python, we only use them
# None is used to declare variables
a = None




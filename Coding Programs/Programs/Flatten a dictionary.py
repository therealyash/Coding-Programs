# Flatten a dictionary

import ast,sys
input_str = sys.stdin.read()
input_dict = dict(ast.literal_eval(input_str))
def flatten_dict(dd, separator='_', prefix=''):
    #complete this function
    return { prefix + separator + k if prefix else k : v 
    for kk, vv in dd.items() 
    for k, v in flatten_dict(vv, separator, kk).items()
    } if isinstance(dd, dict) else { prefix : dd } 

out1=list(flatten_dict(input_dict).keys())
out2=list(flatten_dict(input_dict).values())
out1.sort()
out2.sort()
print(out1)
print(out2)


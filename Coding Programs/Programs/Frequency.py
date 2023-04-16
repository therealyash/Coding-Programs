"""
Write a program that defines a function called frequency() which
computes the frequency of words present in a string passed to it. The
frequencies should be returned in sorted order by words in the string.
"""

def frequency(s):
    new_str = s
    s_list = sorted(new_str.split())
    s_dict = {}

    for i in s_list:
        if i in s_dict:
            s_dict[i] += 1
        else:
            s_dict[i] = 1
    return s_dict

print(frequency('It is true for all that that that \
                 that that that refers to is not the same that \
                 that that that refers to'))











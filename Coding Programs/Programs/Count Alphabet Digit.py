"""
Write a program that defines a function count_alphabets_digits() that accepts a string
and calculates the number of alphabets and digits in it. It should return these values
as a dictionary. Call this function for some sample strings.
"""


def count_alphabet_digits(s):
    new_str = s.replace(" ", "")
    print(new_str)
    alpha_digit_dict = {'alphabets':0, 'digits':0}
    for i in new_str:
        if i.isalpha():
            alpha_digit_dict['alphabets'] += 1
        else:
            alpha_digit_dict['digits'] += 1
    return alpha_digit_dict

print(count_alphabet_digits('ryder 2233'))









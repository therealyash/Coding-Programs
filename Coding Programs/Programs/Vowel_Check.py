# Vowel Check

# Method 1

input_list = ['wood','old','apple','big','item','euphoria']
vowel = 'a','e','i','o','u'
list_vowel =[i for i in input_list if i.startswith(vowel)] # [Type your answer here]
print(list_vowel)

# Method 2

list_vowel =[i for i in input_list if i[0] in 'aeiou']
print(list_vowel)
# Move Vowels

s = 'programming'


def Move_Vowels(s):
    vowel = 'aeiou'
    vowel_str = ''
    conso = ''
    for i in s:
        if i in vowel:
            vowel_str = vowel_str + i
        else:
            conso = conso + i

    return vowel_str + conso

x = Move_Vowels(s)
print(x)



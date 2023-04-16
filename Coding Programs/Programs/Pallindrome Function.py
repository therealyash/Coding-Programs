# Write a function to check whether given string is a pallindrome or not

def isPallindrome(s):
    t = s.lower()
    left = 0
    right = len(t) - 1

    while right >= left:
        if t[left] == '':
            left += 1
        if t[right] == '':
            right -= 1
        if t[left] != t[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPallindrome('Madam'))
print(isPallindrome('yash'))





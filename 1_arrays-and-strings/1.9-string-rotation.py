'''
1.9 String Rotation:
Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring
(e.g., "waterbottle" is a rotation of "erbottlewat").
'''

'''
- concatenate s2 with itself
- check if s1 exists within with a call to isSubstring.
'''

def isSubstring(sub, s): # given helper function (not tested as part of this question).
    '''
    Returns boolean indicating if substr is a substring of s.
    '''

    n, m = len(s), len(sub)
    if m == 0:
        return True
    if m > n:
        return False

    for i in range(n - m + 1):
        # check slice of length m
        if s[i : i + m] == sub:
            return True
    return False

def checkRotation(s1, s2):

    if len(s1) != len(s2):
        return False
    new_s2 = s2 + s2

    return isSubstring(s1, new_s2)


# test case(s).
s1 = "waterbottle"
s2 = "erbottlewat"
assert checkRotation(s1, s2) == True

s1 = "bbb"
s2 = "erbottlewat"
assert checkRotation(s1, s2) == False


s1 = "waterbottle"
s2 = ""
assert checkRotation(s1, s2) == False

s1 = "dedededed"
s2 = "de"
assert checkRotation(s1, s2) == False

print("All test cases passed!")
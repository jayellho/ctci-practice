'''
1.2 Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other.
'''

'''
s1 = abcdefgh
s2 = bddeifh

- count frequencies for both.
- check keys exist in both.
- if all exist, check if count is the same for each key.

'''
import collections

def checkPerm(s1, s2):

    freq_s1 = collections.Counter(s1)
    freq_s2 = collections.Counter(s2)

    for k, v in freq_s1.items():
        if k not in freq_s2 or freq_s2[k] != v:
            return False
    
    for k, v in freq_s2.items():
        if k not in freq_s1 or freq_s1[k] != v:
            return False
    
    return True


# === Test cases ===

s1 = "abcdefgh"
s2 = "bcdefahg"

assert True == checkPerm(s1, s2)

s1 = "abcdefgh"
s2 = "bcdefah"

assert False == checkPerm(s1, s2)

s1 = ""
s2 = "bcdefah"

assert False == checkPerm(s1, s2)

s1 = "bbbbbbb"
s2 = "bcdefah"

assert False == checkPerm(s1, s2)

print("All test cases passed!")
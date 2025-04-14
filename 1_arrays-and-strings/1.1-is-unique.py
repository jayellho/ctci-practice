'''
1.1 Is Unique:
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
'''

def isUnique(s):
    n = len(s)
    if n <= 1:
        return True
    s = list(s)
    s.sort()

    for l in range(n-1):
        r = l + 1
        if s[l] == s[r]:
            return False
    return True

# ==== Test cases ====
s1 = ""
assert True == isUnique(s1)

s2 = "abababa"
assert False == isUnique(s2)

s3 = "abcdefgh"
assert True == isUnique(s3)

print("All test cases passed!")


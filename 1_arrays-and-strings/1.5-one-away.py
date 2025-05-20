'''
1.5 One Away:
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale,   ple     ->  true
pales,  pale    ->  true
pale,   bale    ->  true
pale,   bake    ->  false
'''

'''
- Insert - move one ahead and increment counter.
- Remove - the other should move ahead and increment counter.
- Replace - both move ahead but increment counter.
- Check string lengths.
    - if different, for longer string, increment when chars at position diff and continue comparing.
    - if same, when different, increment both positions.
    - if counter exceeds 1, return false. else, true.

- 
'''

def oneAway(s1, s2):

    n1, n2 = len(s1), len(s2)
    ptr1, ptr2 = 0, 0
    diff_counter = 0

    # edge case 1 - diff in len more than 1.
    if abs(n1 - n2) > 1:
        return False

    while ptr1 < n1 and ptr2 < n2:
        print(ptr1, ptr2, s1[ptr1], s2[ptr2])
        # replace.
        if n1 == n2:
            if s1[ptr1] != s2[ptr2]:
                diff_counter += 1
                
        # insert/remove.
        else:
            if s1[ptr1] != s2[ptr2]:
                diff_counter += 1
                if n1 > n2:
                    ptr1 += 1
                else:
                    ptr2 += 1
        ptr1 += 1
        ptr2 += 1

        # check diff counter.
        if diff_counter > 1:
            print(f"diff_counter = {diff_counter}")
            return False
        
    return True


# test cases.
## 1 - same length strings, valid case.
s1 = "pale"
s2 = "bale"

assert oneAway(s1, s2) == True

# 2 - same length strings, invalid case.
s1 = "pale"
s2 = "bake"

assert oneAway(s1, s2) == False

# 3 - same length strings, invalid case.
s1 = "pale"
s2 = "lepa"

assert oneAway(s1, s2) == False

# 4 - different length strings, valid case.
s1 = "pale"
s2 = "pales"

assert oneAway(s1, s2) == True

# 5 - different length strings, invalid case.
s1 = "pake"
s2 = "pales"

assert oneAway(s1, s2) == False

# 6 - one empty string.
s1 = ""
s2 = "abc"

assert oneAway(s1, s2) == False

# 7 - one empty string, invalid case.
s1 = "a"
s2 = ""

assert oneAway(s1, s2) == True

# 8 - different length strings by more than 1, invalid case.
s1 = "pale"
s2 = "palepale"

assert oneAway(s1, s2) == False
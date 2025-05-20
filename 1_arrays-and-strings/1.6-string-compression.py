'''
1.6 String Compression:
Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3.
If the "compressed" string would not become smaller than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a-z).
'''

'''
- when will the string not be shorter than the original string?
    - abcdefg => 
      a1b1c1d1e1f1g1
    - abccddeeffgg => 
      a1b1c2d2e2f2g2
    - abccccddeeffgg =>
      a1b1c4d2e2f2g2
    - aabbccddeeffgg => 
      a2b2c2d2e2f2g2

- get length of original string.
- create prev pos tracker, curr pos tracker and also curr char tracker.
- while curr pos tracker < len:
    - if curr char tracker != curr char:
        - append to list the curr char tracker, the diff btwn prev and curr pos minus 1
        - set prev pos to curr pos and curr char tracker to curr char
    - else:
        - increment curr pos tracker

- at end, join the list and compare lengths.
'''

def compressString(s):
    # edge case(s)
    ## empty string.
    if not s:
        return s
    
    # define vars.
    n = len(s)
    prevPos, currPos = 0, 0
    charTracking = s[0]
    res = []

    # iterate.
    while currPos < n:
        if charTracking != s[currPos]:
            # update list.
            res.append(charTracking)
            res.append(str(currPos - prevPos))
            
            # housekeeping.
            prevPos = currPos
            charTracking = s[currPos]
        else:
            currPos += 1
    res.append(charTracking)
    res.append(str(currPos - prevPos))

    # create compressed string.
    new_s = "".join(res)
    print(f"compressed: {new_s} (len: {len(new_s)}), original: {s} (len: {len(s)}).")
    
    return new_s if len(new_s) < n else s

# test case(s):
## 1 - compress accepted.
s = "aaabbbcccdddaaa"
assert compressString(s) == "a3b3c3d3a3"

## 2 - compress not accepted.
s = "abcdefgh"
assert compressString(s) == "abcdefgh"

## 3 - compress accepted.
s = "aaaaaaaabbbcccdddabab"
assert compressString(s) == "a8b3c3d3a1b1a1b1"

## 4 - compress accepted.
s = "aaaaAAAAaabbbcccdddabab"
assert compressString(s) == "a4A4a2b3c3d3a1b1a1b1"





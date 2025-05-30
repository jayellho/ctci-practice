'''
10.2 Group Anagrams:
Write a method to sort an array of strings so that all the anagrams are next to each other.
'''

'''
[ santa, satan, mono, moon ]

- how do we know they are anagrams of each other? they have the same character counts.
- assuming length of word is k, if we sort it alphabetically, it's k log k. n words. so, O(n * k log k), then put into dictionary.
- alternatively:
    - count frequencies of each word O(n * k)
    - for each word, compare to the item in the dictionary. O(n)
'''
import collections

# main method.
def groupAnagrams(strArr):

    # assuming only lowercase ascii chars.
    ## get char counts. and store in dictionary as tuple.
    # overallDict = collections.defaultdict(list)
    # for word in strArr:
    #     chars = [0] * 26
    #     for char in word:
    #         chars[ord(char) - ord('a')] += 1
        
    #     overallDict[tuple(chars)].append(word)
    
    # res = []
    # for k, v in overallDict.items():
    #     res.extend(v)
    # print(overallDict)
    # return res


    # assuming any characters.
    # overallDict = collections.defaultdict(list)
    # for word in strArr: # outer loop: O(n)
    #     chars = {}
    #     for char in word: # inner loop: O(k)
    #         if char not in chars:
    #             chars[char] = 1
    #         else:
    #             chars[char] += 1
        
    #     tuple_chars = []
    #     for k, v in chars.items(): # inner loop: O(1)
    #         tuple_chars.append((k,v))
        
    #     overallDict[tuple(sorted(tuple_chars))].append(word) 
    
    # res = []
    # for v in overallDict.values():
    #     res.extend(v)

    # return res

    # alternative approach - sort chars and use as keys in a dictionary.
    def sortChars(word):
        return "".join(sorted(word))
    
    overallDict = collections.defaultdict(list)

    for word in strArr:
        wordSorted = sortChars(word)
        overallDict[wordSorted].append(word)
    
    res = []
    for v in overallDict.values():
        res.extend(v)

    return res
            


# test cases:
strArr = [ "satan", "mono", "moon", "santa" ]
res = groupAnagrams(strArr)
print(res)







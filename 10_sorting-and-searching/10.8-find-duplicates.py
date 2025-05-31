'''
10.8 Find Duplicates: 
You have an array with all the numbers from 1 to N, where N is at most 32,000. 
The array may have duplicate entries and you do not know what N is. 
With only 4 kilobytes of memory available, how would you print all duplicate elements in the array?
'''

'''
1 byte = 8 bits
bit = 0 or 1
4 kb = 2 ^ 15 = 32000

use a bit vector of size 32000 bits
go through each element in the array, and set them to 1 if they were 0.
if already 1, print them.

READ CTCI FOR DETAILED ANSWER.
'''
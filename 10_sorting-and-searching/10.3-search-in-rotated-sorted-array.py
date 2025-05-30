'''
10.3 Search in Rotated Array: 
Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. 
You may assume that the array was originally sorted in increasing order.

EXAMPLE
Input: find 5 in {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
Output: 8 (the index of 5 in the array)
'''

'''
- modified binary search.
- we need to know whether we are in the R or L array.
'''
# solution 1: find pivot with bin search, then do usual bin search ==> O(log n) but bin search run twice.
# def getPivot(arr):
#     # we want to be the smallest element in the right arr if it is rotated.
#     ## edge case: not rotated.
#     if arr[0] < arr[-1]:
#         return 0
#     low = 0
#     high = len(arr)-1

#     while low <= high:
#         mid = (high + low) // 2
        
#         # check if in R array.
#         if arr[0] > arr[mid]:
#             # if in R arr, move left until arr[mid-1] > arr[mid]
#             if arr[mid-1] <= arr[mid]:
#                 high = mid - 1
#             else:
#                 return mid
#         else:
#             low = mid + 1

# def binSearchRotated(arr, target):
#     pivot = getPivot(arr)

#     # case: arr not rotated.
#     if pivot == 0:
#         low = 0
#         high = len(arr)-1

#     # case: arr is rotated ==> check if target is on left or right.
#     elif target < arr[0]:
#         low = pivot
#         high = len(arr)-1
#     elif target == arr[0]:
#         return 0
#     else:
#         low = 0
#         high = pivot

#     # do the usual binary search.
#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] < target:
#             low = mid + 1
#         elif arr[mid] > target:
#             high = mid - 1
#         else:
#             return mid
#     return -1

# solution 2: just do one modified bin search.
def binSearchRotated(arr, target):
    '''
    scenarios:
    1. arr is not rotated.
        just set target and curr to be in the same segment.


    2. arr is rotated.
        a. target is in L <== target > rightmost elem.
            check if curr is in L or R. if L, move R if smaller than target, move L if bigger than target. if R, move left.
        b. target is in R <== target < leftmost elem.
            check if curr is in L or R. if R, move R if smaller than target, move L if bigger than target. if L, move right.
    '''
    # check where target is. if not rotated, default to L.
    targetInL = True
    if target < arr[0]:
        targetInL = False
    
    # do modified binary search.
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        currInL = arr[mid] >= arr[0]

        # check if curr is in same half as target ==> do usual binary search.
        if (not currInL and not targetInL) or (currInL and targetInL):
            if arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                return mid
        
        # move to correct half if target and curr are different halves.
        else:
            # target in R, curr in L ==> move R.
            if not targetInL and currInL:
                low = mid + 1
            else:
                high = mid - 1
        
    return -1
    









# test cases:
# rotated arr, target in right side. 
arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
res = binSearchRotated(arr, 10)
assert res == 10

# rotated arr, target as first element.
arr = [15, 16, 19, 1, 3, 4, 5, 7, 10, 14]
res = binSearchRotated(arr, 15)
assert res == 0


# rotated arr, target in left side.
arr = [15, 16, 19, 1, 3, 4, 5, 7, 10, 14]
res = binSearchRotated(arr, 16)
assert res == 1

# rotated arr, target in rightmost.
arr = [15, 16, 19, 1, 3, 4, 5, 7, 10, 14]
res = binSearchRotated(arr, 14)
assert res == 9

# arr not rotated, target somewhere in middle.
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = binSearchRotated(arr, 7)
assert res == 4

# arr not rotated, target rightmost
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = binSearchRotated(arr, 19)
assert res == 9

# arr not rotated, target leftmost
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = binSearchRotated(arr, 1)
assert res == 0


# arr not rotated, target does not exist
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = binSearchRotated(arr, 100)
assert res == -1

# arr not rotated, duplicate values
arr = [1, 3, 3, 4, 5, 7, 7, 10, 14, 15, 16, 19]
res = binSearchRotated(arr, 10)
assert res == 7

# rotated arr, duplicate values
arr = [15, 16, 16, 16, 19, 1, 3, 4, 5, 7, 10, 14, 14]
res = binSearchRotated(arr, 1)
assert res == 5

print("All test cases passed!")
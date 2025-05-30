'''
10.4 Sorted Search, No Size: 
You are given an array-like data structure Listy which lacks a size method. 
It does, however, have an elementAt(i) method that returns the element at index i in 0(1) time. 
If i is beyond the bounds of the data structure, it returns -1.
(For this reason, the data structure only supports positive integers.) 
Given a Listy which contains sorted, positive integers, find the index at which an element x occurs. 
If x occurs multiple times, you may return any index.
'''

'''
- we don't know the high.
- double each time and check the element at i. so 1 => 2 => 4 => 8 => 16 etc. < O (log n)
- stop at the point when either elem is -1 or elem > x.
- do binary search with the point before that point and the point.

'''
def elementAt(arr, i):
    if i >= len(arr):
        return -1
    else:
        return arr[i]
def sortedNoSizeSearch(arr, x):
    # # edge case: x is first element.
    # if arr[0] == x:
    #     return 0

    low = 0
    high = 0
    while elementAt(arr, high) != -1 and elementAt(arr, high) <= x:
        if high == 0:
            high = 1
            low = 0
        else:
            low = high
            high *= 2

    
    while low <= high:
        mid = (low + high) // 2
        if elementAt(arr, mid) == -1 or elementAt(arr, mid) > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            return mid
    return -1


# arr not rotated, target somewhere in middle.
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = sortedNoSizeSearch(arr, 7)
assert res == 4

# arr not rotated, target rightmost
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = sortedNoSizeSearch(arr, 19)
assert res == 9

# arr not rotated, target leftmost
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = sortedNoSizeSearch(arr, 1)
assert res == 0

# arr not rotated, target not in arr
arr = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19]
res = sortedNoSizeSearch(arr, 500)
assert res == -1

print("All test cases passed!")
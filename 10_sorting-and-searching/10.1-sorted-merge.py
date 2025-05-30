'''
10.1 Sorted Merge: 
You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. 
Write a method to merge B into A in sorted order.
'''
'''
- make use of the sorted nature of both arrays.
- reminds me of the merge operation in mergesort.
- A, B in ascending order.
- start from the end of both arrays, and decrease until 0. inserting from the back.
    - compare and pick the larger number than move the pointers.
'''


def sortedMerge(a, b):

    n = len(a)
    ptrB = len(b) - 1
    ptrA = n - len(b) - 1


    for i in range(n-1, -1, -1):
        # do comparison of items at pointers.
        if ptrA >= 0 and ptrB >= 0:
            if a[ptrA] > b[ptrB]:
                a[i] = a[ptrA]
                ptrA -= 1
            else:
                a[i] = b[ptrB]
                ptrB -= 1
        elif ptrA < 0:
            a[i] = b[ptrB]
            ptrB -= 1
        else:
            a[i] = a[ptrA]
            ptrA -= 1
    
    return a



    



a = [2,4,5,7,9,11,0,0,0]
b = [3,6,8]

sortedL = sortedMerge(a, b)
print(sortedL)
import random

def partition(s, low, high):
    less = low # marks point to insert elem < s[p]

    # # procedure to randomise the selection of partition.
    # p = random.randint(low, high-1)
    # print(f"randomised p = {p}")
    # s[p], s[high-1] = s[high-1], s[p]
    # p = high -1

    p = high - 1

    # iterate through selected part of array.
    for i in range(low, high):
        # if curr index smaller than s[p], we want to record it in less.
        if s[i] <= s[p]:
            # we also want to check whether we should swap curr with less. pushes smaller elems left.
            if s[i] < s[less]:
                s[i], s[less] = s[less], s[i]
            less += 1
    return less-1


def quicksort(s, low, high):
    if low >= high:
        return
    
    p = partition(s, low, high)

    quicksort(s, low, p)
    quicksort(s, p+1, high)

    # return s

s = [3,2,5,0,1,8,7,6,9,4]
quicksort(s, 0, len(s))
print(s)


s = [1, 7, 5, 3, 2, 11, 2, 9, 6]
quicksort(s, 0, len(s))
print(s)


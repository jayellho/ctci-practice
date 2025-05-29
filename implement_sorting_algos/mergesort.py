def mergeSort(s, low, high):

    # continue splitting if low < high
    # print(s[low:high+1])
    if low < high:
        mid = (low + high) // 2

        l1 = mergeSort(s, low, mid)
        l2 = mergeSort(s, mid+1, high)

        return merge(l1, l2)
    return s[low:high+1]
    
def merge(l1, l2):
    '''
    - given two sorted lists, merge them in sorted order.
    - compare each element in both lists then insert into a new list.
    '''

    res = []
    ptr1, ptr2 = 0, 0
    n1, n2 = len(l1) if l1 else 0, len(l2) if l2 else 0

    while ptr1 < n1 or ptr2 < n2:
        if ptr1 == n1:
            res.append(l2[ptr2])
            ptr2 += 1
        elif ptr2 == n2:
            res.append(l1[ptr1])
            ptr1 += 1
        else:
            if l1[ptr1] < l2[ptr2]:
                res.append(l1[ptr1])
                ptr1+= 1
            else:
                res.append(l2[ptr2])
                ptr2+= 1
    
    return res


l = [1,3,2,4,7,6,5]
n = len(l)
sorted_l = mergeSort(l, 0, n) 
print(f"original: {l}, sorted: {sorted_l}")

l = [3,3,3,1,1,1,2,2,2]
n = len(l)
sorted_l = mergeSort(l, 0, n) 
print(f"original: {l}, sorted: {sorted_l}")

l = [9,8,7,6,5,4,3,2,1]
n = len(l)
sorted_l = mergeSort(l, 0, n) 
print(f"original: {l}, sorted: {sorted_l}")

'''
2.2 Return Kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list.
'''

'''
0 -> 1 -> 2 -> 3 -> 4 -> None

- create two pointers pointing to the head of the linked list.
- move the first pointer k times.
- move both pointers until the first pointer hits the last element in the list.
- return the second pointer.


'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# iterative solution.
def getKthToLast(head, k):

    fast, slow = head, head

    # move fast pointer ahead.
    for _ in range(k):
        fast = fast.next

    # move both pointers.
    while fast:
        fast = fast.next
        slow = slow.next
    
    print(f"kth to last elem val: {slow.val}")
    
    return slow

# recursive solution.
def getKthToLast(head, k):

    if not head:
        return 0

    idx = getKthToLast(head.next, k) + 1

    if idx == k:
        print(f"kth to last elem val: {head.val}") # only prints; if want to return something, modify function.
    
    return idx
        

# test cases.
## 1 - when k is 1.
llist = Node(1, next=Node(2, next=Node(3, next=Node(4))))
k = 1
getKthToLast(llist, k)

## 2 - when k is 2.
llist = Node(1, next=Node(2, next=Node(3, next=Node(4))))
k = 2
getKthToLast(llist, k)


'''
2.1 Remove Dups:
Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''

'''
- duplicates: nodes with duplicate values?
0 -> 1 -> 2 -> 3 -> 4 -> 1

with temporary buffer:
- two pointers, one prev and one current.
- buffer is a set containing values.
- if curr.val in buffer, remove it - set prev.next to curr.next and set curr to curr.next
'''

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def printLL(head, status):
    print(f"{status}:")
    while head:
        print(head.val, end=" ")
        head = head.next
    print("\n")


def removeDups(head):

    # create vars.
    seen = set()
    prev, curr = head, head

    # iterate.

    while curr:
        # curr ptr not seen before, add to seen.
        if curr.val not in seen:
            seen.add(curr.val)
            prev = curr # only update if no changes; if update when curr deleted, will go to the alr-deleted curr.
        
        # if seen before, delete it.
        else:
            prev.next = curr.next
        
        curr = curr.next

    return head


# test case(s):
## 1
testList = Node(1, next=Node(2, next=Node(4, next=Node(2, next=Node(3, next=Node(2, next=Node(4)))))))
printLL(testList, "original")
modList = removeDups(testList)
printLL(modList, "modified")

## 2
testList = Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2)))))))
printLL(testList, "original")
modList = removeDups(testList)
printLL(modList, "modified")

## 3
testList = Node(1)
printLL(testList, "original")
modList = removeDups(testList)
printLL(modList, "modified")

## 4
testList = None
printLL(testList, "original")
modList = removeDups(testList)
printLL(modList, "modified")


## 5
testList = Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2))))))))))))))
printLL(testList, "original")
modList = removeDups(testList)
printLL(modList, "modified")


## 6
testList = Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(1, next=Node(2, next=Node(2, next=Node(2, next=Node(2, next=Node(2))))))))))))))
printLL(testList, "original")
modList = removeDups(testList)
printLL(modList, "modified")


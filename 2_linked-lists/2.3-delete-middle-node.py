'''
2.3 Delete Middle Node:
Implement an algorithm to delete a node in the middle 
(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.

EXAMPLE
Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''

'''
- copy next node into current node.
- this works because we know the node to remove is not in the beginning or the end.
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

def delMiddleNode(x):
    tmp = x.next

    x.val = tmp.val
    x.next = tmp.next


# test case(s):
## 1
testList = Node(1, next=Node(2, next=Node(4, next=Node(5, next=Node(3, next=Node(6, next=Node(7)))))))
x = Node(5, next=Node(3, next=Node(6, next=Node(7))))
printLL(x, "original")
delMiddleNode(x)
printLL(x, "modified")




'''
2.5 Sum Lists:
You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1's digit is at the head of the list.
Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
Output: 9 -> 1 -> 2. That is, 912.
'''

'''
ORIGINAL (STORED IN REVERSE ORDER)
- two pointers for each.
- they may have diff lengths. iterate until both reach none.
- there may be an additional node needed.
- sum at each point + carryover.

VARIATION (STORED IN FORWARD ORDER)
- 
'''

# helper functions ==============================================================================
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

# main function =================================================================================
## original: reversed order - ITERATIVE
def sumLists(list1, list2):
    new = Node()
    ptr = new
    carry = 0
    while list1 or list2:
        curr_sum = carry
        if list1:
            curr_sum += list1.val
            list1 = list1.next
        
        if list2:
            curr_sum += list2.val
            list2 = list2.next
        
        carry = curr_sum // 10
        curr_sum %= 10
        ptr.next = Node(curr_sum)
        ptr = ptr.next
    
    if carry > 0:
        ptr.next = Node(carry)
    
    return new.next

## TODO: variation: forward order
# def sumLists(list1, list2):
#     pass

## TODO: original: reversed order - RECURSIVE
# def sumLists(list1, list2):
#     pass

# test case(s) ==================================================================================
list1 = Node(7, next=Node(1, next=Node(6)))
list2 = Node(5, next=Node(5, next=Node(2)))
res = sumLists(list1, list2)
printLL(res, "result")

list1 = Node(7, next=Node(1, next=Node(6)))
list2 = Node(5, next=Node(9, next=Node(2)))
res = sumLists(list1, list2)
printLL(res, "result")

list1 = Node(9, next=Node(9, next=Node(9)))
list2 = Node(9, next=Node(9, next=Node(9)))
res = sumLists(list1, list2)
printLL(res, "result")

list1 = Node(9, next=Node(9, next=Node(9, next=Node(1, next=Node(9)))))
list2 = Node(9, next=Node(9, next=Node(9)))
res = sumLists(list1, list2)
printLL(res, "result")

list1 = Node(9, next=Node(9, next=Node(9, next=Node(1))))
list2 = Node(9, next=Node(9, next=Node(9, next=Node(9, next=Node(1)))))
res = sumLists(list1, list2)
printLL(res, "result")

list1 = Node(9, next=Node(9, next=Node(9, next=Node(1))))
list2 = None
res = sumLists(list1, list2)
printLL(res, "result")
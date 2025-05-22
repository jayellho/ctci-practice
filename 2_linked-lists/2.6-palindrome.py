'''
2.6 Palindrome:
Implement a function to check if a linked list is a palindrome.
'''

'''
1 -> 2 -> 3 -> 2 -> 1
0    1    2    3    4

1 -> 4 -> 4 -> 1
0    1    2    3

0 1 2
0 2 None

- two pointers - one fast (2x), one slow (1x)
- when fast hits None, that should be mid point.
- as slow iterates, store in stack.
- at midpoint, compare each value with popped item from stack and return result.
'''
# helper functions =================================================================
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# main function =====================================================================
def checkPalindrome(head):
    fast, slow = head, head
    stack = []

    # get midpoint and reverse values.
    while fast:
        # store slow value in stack.
        stack.append(slow.val)
        
        # check if odd or even length.
        ## if even, slow remains. else, slow increment by 1.
        if not fast.next: # means even length.
            break
        else: # means odd length.
            slow = slow.next
        fast = fast.next.next
        # slow = slow.next

    # compare values from 2nd half of linked list with values from stack.
    while slow:
        popped = stack.pop()
        if popped != slow.val:
            return False
    
        slow = slow.next
    
    return True

# TODO: Recursive implementation!

# test case(s) =======================================================================
test = Node(1, next=Node(2, next=Node(2, next=Node(1))))
assert checkPalindrome(test) == True

test = Node(1, next=Node(2, next=Node(3, next=Node(3, next=Node(1)))))
assert checkPalindrome(test) == False

test = Node(1, next=Node(2, next=Node(2, next=Node(1))))
assert checkPalindrome(test) == True

test = Node(1, next=Node(2, next=Node(3, next=Node(2, next=Node(1)))))
assert checkPalindrome(test) == True

test = Node(1)
assert checkPalindrome(test) == True

test = Node(1, next=Node(2, next=Node(3, next=Node(4, next=Node(4, next=Node(3, next=Node(2, next=Node(1))))))))
assert checkPalindrome(test) == True

print(f"All test cases passed!")
'''
2.4 Partition:
Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.
If x is contained within the list, the values of x only need to be after the elements less than x (see below).
The partition element x can appear anywheree in the "right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition=5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

'''
- two pointers - one for L, one for R.
- create a new linked list.
- move L until the end and add, then R.

OR

- one pointer.
- create 2 new linked lists - one for L, one for R.
- move pointer and append to respective lists.
- join the lists.
'''
# helper functions ==============================
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

def build_ll(vals):
    """Builds a linked list from a Python list of values and returns its head."""
    head = None
    tail = None
    for v in vals:
        node = Node(v)
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def to_list(head):
    """Converts a linked list back into a Python list of values."""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out

def run_partition_tests():
    tests = [
        # format: (input_list, partition_x, expected_output_list)
        ([],               5, []),                   # empty list
        ([1],              1, [1]),                  # single node equal to x
        ([1],              0, [1]),                  # single node greater than x
        ([1],              2, [1]),                  # single node less than x
        ([3,5,8,5,10,2,1], 5, [3,2,1,5,8,5,10]),      # example from prompt
        ([5,5,5],          5, [5,5,5]),              # all equal to x
        ([1,2,3],          5, [1,2,3]),              # all less than x
        ([6,7,8],          5, [6,7,8]),              # all greater than x
        ([2,5,1,5,2],      2, [1,2,5,5,2]),          # x at head and tail
        ([0,-1,3,2,-2],    0, [-1,-2,0,3,2]),        # negatives mixed
    ]

    for idx, (vals, x, expected) in enumerate(tests, 1):
        head = build_ll(vals)
        modified = partitionLinkedList(head, x)
        out = to_list(modified)
        print(f"Test #{idx}: input={vals}, x={x}")
        print(f"  → got     {out}")
        print(f"  → expected{expected}")
        assert out == expected, f"❌ Test #{idx} failed!"
    print("🎉 All tests passed!")

# main function ==================================

def partitionLinkedList(head, x):
    ptr = head
    left, right = Node(), Node()
    l_ptr, r_ptr = left, right


    while ptr:
        if ptr.val < x:
            tmp = Node(ptr.val)
            l_ptr.next = tmp
            l_ptr = l_ptr.next
            
        else:
            tmp = Node(ptr.val)
            r_ptr.next = tmp
            r_ptr = r_ptr.next

        ptr = ptr.next

    # combine lists.
 
    right = right.next
    l_ptr.next = right

    return left.next   




# run tests:
run_partition_tests()


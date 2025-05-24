'''
2.7 Intersection:
Given two (singly) linked lists, determine if the two lists intersect.
Return the intersecting node.
Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list,
then they are intersecting.
'''

'''
- don't know length of linked lists.
- METHOD 1:
    - iterate through both lists to get length. << O (n) where n is the longer list.
    - get difference in length, and for longer list, iterate till difference. << O(k) where k is the difference.
    - then compare each node from there. << O (m)
'''
# define helper functions.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# define main function.
# def getIntersection(node1, node2): # leetcode's optimal solution.
#     ptr1, ptr2 = node1, node2

#     while ptr1 != ptr2:
#         ptr1 = node2 if not ptr1 else ptr1.next
#         ptr2 = node1 if not ptr2 else ptr2.next
    
#     return ptr1

def getIntersection(node1, node2): # my solution.
    len1, len2 = 0, 0
    ptr1, ptr2 = node1, node2

    # get lengths of both linked lists.
    while ptr1:
        len1 += 1
        ptr1 = ptr1.next

    while ptr2:
        len2 += 1
        ptr2 = ptr2.next

    # fast forward the longer list (if there is) then compare from there.
    if len1 >= len2:
        longer = node1
        shorter = node2
    else:
        longer = node2
        shorter = node1
    
    diff = abs(len1 - len2)

    for _ in range(diff):
        longer = longer.next
    
    while longer:
        # print(f"longer = {longer.val}, shorter = {shorter.val}")
        if longer == shorter:
            return longer
        longer = longer.next
        shorter = shorter.next
    
    return None

# test case(s):
def run_tests():
    tests = []

    # 1) No intersection, both non-empty
    l1 = Node(1, next=Node(2, next=Node(3)))
    l2 = Node(4, next=Node(5, next=Node(6)))
    tests.append(("No intersection", l1, l2, None))

    # 2) Intersection in the middle
    shared = Node(7, next=Node(8, next=Node(9)))
    l1 = Node(1, next=Node(2, next=shared))
    l2 = Node(3, next=Node(4, next=Node(5, next=shared)))
    tests.append(("Middle intersection", l1, l2, shared))

    # 3) Intersection at head (identical lists)
    shared = Node(10, next=Node(11))
    l1 = shared
    l2 = shared
    tests.append(("Head intersection (identical lists)", l1, l2, shared))

    # 4) Intersection at tail (only last node shared)
    shared = Node(12)
    l1 = Node(6, next=Node(7, next=Node(8, next=shared)))
    l2 = Node(9, next=shared)
    tests.append(("Tail intersection", l1, l2, shared))

    # 5) One list empty
    l1 = None
    l2 = Node(13, next=Node(14))
    tests.append(("One empty list", l1, l2, None))

    # 6) Both lists empty
    l1 = None
    l2 = None
    tests.append(("Both empty lists", l1, l2, None))

    # run them
    for name, n1, n2, expected in tests:
        result = getIntersection(n1, n2)
        ok = result is expected
        got = result.val if result else None
        exp = expected.val if expected else None
        status = "PASS" if ok else f"FAIL (got {got}, expected {exp})"
        print(f"{name}: {status}")

if __name__ == "__main__":
    run_tests()
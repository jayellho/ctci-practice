'''
2.8 Loop Detection:
Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C
'''
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def detectLoop(head):

    fast, slow = head, head
    
    # get collision point.
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            break
    
    # handle when there is no collision - meaning no loop.
    if not fast or not fast.next:
        return None

    # get start of loop.
    slow = head
    while slow != fast:
        slow = slow. next
        fast = fast.next
    
    return fast


# test case(s) - chatgpt.
def run_loop_tests():
    tests = []

    # 1) Empty list
    tests.append(("Empty list", None, None))

    # 2) Single node, no loop
    n1 = Node(1)
    tests.append(("Single node without loop", n1, None))

    # 3) Single node, self-loop
    n2 = Node(2)
    n2.next = n2
    tests.append(("Single node with self-loop", n2, n2))

    # 4) Multi-node, no loop
    a = Node('A', next=Node('B', next=Node('C', next=Node('D'))))
    tests.append(("Multiple nodes without loop", a, None))

    # 5) Loop starts in the middle (E → C)
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    A.next, B.next, C.next, D.next, E.next = B, C, D, E, C
    tests.append(("Loop in middle (E→C)", A, C))

    # 6) Loop back to head (D → A)
    X = Node('X')
    Y = Node('Y')
    Z = Node('Z')
    X.next, Y.next, Z.next = Y, Z, X
    tests.append(("Loop to head (Z→X)", X, X))

    # 7) Two-node loop (B → A)
    p = Node('p')
    q = Node('q')
    p.next = q
    q.next = p
    tests.append(("Two-node loop (q→p)", p, p))

    # run them
    for name, head, expected in tests:
        result = detectLoop(head)
        ok = result is expected
        got = result.val if result else None
        exp = expected.val if expected else None
        status = "PASS" if ok else f"FAIL (got {got}, expected {exp})"
        print(f"{name}: {status}")

if __name__ == "__main__":
    run_loop_tests()
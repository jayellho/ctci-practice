'''
4.10 Check Subtree:
T1 and T2 are very large binary trees, with T1 much bigger than T2.
Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkSubtree(t1, t2):
    # T1 subtree of T2?

    ''' 
    rough algo:
    - do a preorder traversal of both trees, storing null nodes too - O(n).
    - do a substring check of the generated lists.
        
    '''
    # method 1: time complexity = O(m + n), space complexity = O(m + n)
    # def getPreorder(node, res):

    #     if not node:
    #         res.append('X')
    #         return res
        
    #     res.append(str(node.val))
    #     getPreorder(node.left, res)
    #     getPreorder(node.right, res)
    #     return res


    # t1_list = getPreorder(t1, [])
    # t2_list = getPreorder(t2, [])

    # t1_str = " ".join(t1_list)
    # t2_str = " ".join(t2_list)

    # return t2_str in t1_str

    # method 2
    def matchTrees(s1, s2):
        if not s2:
            return True
        if not s1 and s2:
            return False
        
        return s1.val == s2.val and (matchTrees(s1.left, s2.left) and matchTrees(s1.right, s2.right))
    
    compare = [False]
    def recurse(t1, t2):
        if not t1 or not t2:
            return
        
        if t1.val == t2.val and matchTrees(t1,t2):
            compare[0] = True
        
        recurse(t1.left, t2)
        recurse(t1.right, t2)

    if not t2:
        return True
    recurse(t1, t2)
    return compare[0]

    
    


# test case(s):
# --- Test Trees ---

# Test 1: T1 is a larger tree.
#       1
#      / \
#     2   3
#    /   / \
#   4   5   6
#      / \
#     7   8
#         \
#          9
T1 = Node(1,
          left=Node(2, left=Node(4)),
          right=Node(3,
                     left=Node(5, left=Node(7), right=Node(8)),
                     right=Node(6, right=Node(9))))

# T2_sub: A subtree of T1 (subtree rooted at node 5)
#      5
#     / \
#    7   8
T2_sub = Node(5, left=Node(7), right=Node(8))

# Test 2: T2_not: A tree that is NOT a subtree of T1.
#      3
#     / \
#    7   8
# Although T1 has 3, 7, and 8, node 3 in T1 has different children.
T2_not = Node(3, left=Node(7), right=Node(8))

# Test 3: T2_empty: An empty tree (should be a subtree by definition)
T2_empty = None

# Test 4: T2_equal: Exactly the same tree as T1.
T2_equal = T1

# Test 5: T1_empty is empty, but T2 is non-empty.
T1_empty = None
T2_non_empty = Node(1)

# --- Assertions to verify is_subtree ---
assert checkSubtree(T1, T2_sub) == True, "T2_sub should be a subtree of T1"
assert checkSubtree(T1, T2_not) == False, "T2_not should NOT be a subtree of T1"
assert checkSubtree(T1, T2_empty) == True, "An empty tree is considered a subtree of any tree"
assert checkSubtree(T1, T2_equal) == True, "T2_equal is identical to T1"
assert checkSubtree(T1_empty, T2_non_empty) == False, "A non-empty tree cannot be a subtree of an empty tree"

print("All tests passed!")



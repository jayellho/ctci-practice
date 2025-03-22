'''
4.6 Successor:
Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a binary search tree.
You may assume that each node has a link to its parent.
'''

'''
- 
'''

# define classes.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# define functions.
def successor_value(givenNode, binTree):

    # solution 1: not as optimized and doesn't use L < node < R property of BST.
    # res = [-1]
    # def recurse(node, closestLParent):

    #     if not node:
    #         return
        
        
    #     if node.val == givenNode:
    #         if not node.right:
    #             res[0] = closestLParent.val if closestLParent else None
    #             return
    #         else:
    #             tmp = node.right
    #             while tmp.left:
    #                 tmp = tmp.left
                
    #             res[0] = tmp.val
    #             return
        
    #     recurse(node.left, node)
        
    #     recurse(node.right, closestLParent)
    
    # recurse(binTree, None)
    # print(f"givenNode = {givenNode}, successor = {res[0]}")
    # return res[0]



    # solution 2: uses L < node < R property of BST.
    res = None
    while binTree:

        if givenNode < binTree.val:
            res = binTree.val
            binTree = binTree.left
        else:
            binTree = binTree.right
    return res

# test cases.
## 1
tree = Node(3, left=Node(1, right=Node(2)), right=Node(6, left=Node(4, right=Node(5)), right=Node(8,left=Node(7), right=Node(9))))
successor_value(1, tree)

# Test cases with assertions:

# Test case 1: Original tree example.
# Tree structure (in-order): 1, 2, 3, 4, 5, 6, 7, 8, 9
tree = Node(3, 
            left=Node(1, right=Node(2)), 
            right=Node(6, left=Node(4, right=Node(5)), right=Node(8, left=Node(7), right=Node(9))))
assert successor_value(1, tree) == 2, "Test case 1 failed: successor of 1 should be 2."

# Test case 2: Single node tree.
single_tree = Node(10)
assert successor_value(10, single_tree) is None, "Test case 2 failed: successor of 10 should be None."

# Test case 3: Left-skewed tree.
# Tree structure (in-order): 1, 2, 3, 5
tree2 = Node(5, left=Node(3, left=Node(2, left=Node(1))))
assert successor_value(2, tree2) == 3, "Test case 3 failed: successor of 2 should be 3."
assert successor_value(5, tree2) is None, "Test case 3 failed: successor of 5 should be None."

# Test case 4: Right-skewed tree.
# Tree structure (in-order): 1, 2, 3, 4
tree3 = Node(1, right=Node(2, right=Node(3, right=Node(4))))
assert successor_value(2, tree3) == 3, "Test case 4 failed: successor of 2 should be 3."
assert successor_value(4, tree3) is None, "Test case 4 failed: successor of 4 should be None."

# Test case 5: A balanced BST.
# Tree structure:
#         20
#        /  \
#      10    30
#     /  \   / \
#    5   15 25  35
# In-order: [5, 10, 15, 20, 25, 30, 35]
tree4 = Node(20, 
             left=Node(10, left=Node(5), right=Node(15)), 
             right=Node(30, left=Node(25), right=Node(35)))
assert successor_value(15, tree4) == 20, "Test case 5 failed: successor of 15 should be 20."
assert successor_value(10, tree4) == 15, "Test case 5 failed: successor of 10 should be 15."
assert successor_value(35, tree4) is None, "Test case 5 failed: successor of 35 should be None."

# Test case 6: A more complex BST.
# Tree structure:
#             50
#           /    \
#         30      70
#        /  \    /  \
#      20   40  60   80
#     /      \
#   10       45
# In-order: [10, 20, 30, 40, 45, 50, 60, 70, 80]
tree5 = Node(50, 
             left=Node(30, left=Node(20, left=Node(10)), right=Node(40, right=Node(45))),
             right=Node(70, left=Node(60), right=Node(80)))
assert successor_value(40, tree5) == 45, "Test case 6 failed: successor of 40 should be 45."
assert successor_value(45, tree5) == 50, "Test case 6 failed: successor of 45 should be 50."
assert successor_value(80, tree5) is None, "Test case 6 failed: successor of 80 should be None."

print("All tests passed!")
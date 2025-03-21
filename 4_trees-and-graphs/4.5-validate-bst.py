'''
4.5 Validate BST:
Implement a function to check if a binary tree is a binary search tree.
'''

'''
BST if:
- all L elems in all subtrees < parent < all R elems in all subtrees.

algo:
- try recursion!
- 
'''

# define classes.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define functions.
def validateBST(binTree):

    def recurse(node, l_range, r_range):
        # base case(s)
        if not node:
            return True
        
        if node.val < l_range or node.val > r_range:
            return False
        

        left = recurse(node.left, l_range, node.val)
        right = recurse(node.right, node.val, r_range)

        return left and right
    return recurse(binTree, -float('inf'), float('inf'))

# test cases.
def run_tests():
    # Grouping test cases as tuples: (test_name, tree, expected_result)
    test_cases = [
        (
            "Test Case 1 - valid BST (balanced)",
            TreeNode(4,
                     left=TreeNode(2,
                                   left=TreeNode(1),
                                   right=TreeNode(3)),
                     right=TreeNode(6,
                                    left=TreeNode(5),
                                    right=TreeNode(7))),
            True
        ),
        (
            "Test Case 2 - valid BST (single node)",
            TreeNode(10),
            True
        ),
        (
            "Test Case 3 - invalid BST (right child less than root)",
            TreeNode(10,
                     left=TreeNode(5),
                     right=TreeNode(8)),
            False
        ),
        (
            "Test Case 4 - invalid BST (violation in right subtree)",
            TreeNode(10,
                     left=TreeNode(5),
                     right=TreeNode(15,
                                    left=TreeNode(6),  # 6 is less than 10; violation!
                                    right=TreeNode(20))),
            False
        ),
        (
            "Test Case 5 - valid BST (left-skewed)",
            TreeNode(5,
                     left=TreeNode(3,
                                   left=TreeNode(1))),
            True
        )
    ]

    for name, tree, expected in test_cases:
        result = validateBST(tree)
        assert result == expected, f"{name} failed: expected {expected}, got {result}"
        print(f"{name} passed!")

# Run all tests
run_tests()

'''
4.4 Check Balanced:
Implement a function to check if a binary tree is balanced. 
For the purposes of this question, 
a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
'''

# define classes.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# define function.
def checkBalanced(binTree:TreeNode)->bool:

    def recurse(node):
        # base case(s).
        if not node:
            return 0

        left = recurse(node.left)
        right = recurse(node.right)

        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        else:
            return max(left, right) + 1

    res = recurse(binTree)
    return res != -1


# test cases.
def run_tests():
    # Grouping test cases: each tuple is (test_name, tree, expected_result)
    test_cases = [
        (
            "Test Case 1 - imbalanced",
            TreeNode(1,
                     left=TreeNode(2,
                                   left=TreeNode(3,
                                                 left=TreeNode(6),
                                                 right=TreeNode(7)),
                                   right=TreeNode(4)),
                     right=TreeNode(5,
                                    left=TreeNode(8),
                                    right=TreeNode(9,
                                                   left=TreeNode(10)))),
            True
        ),
        (
            "Test Case 2 - imbalanced",
            TreeNode(1,
                     left=TreeNode(2,
                                   left=TreeNode(3,
                                                 left=TreeNode(6),
                                                 right=TreeNode(7)),
                                   right=TreeNode(4)),
                     right=TreeNode(5,
                                    right=TreeNode(9,
                                                   left=TreeNode(10)))),
            False
        ),
        (
            "Test Case 3 - imbalanced",
            TreeNode(1,
                     TreeNode(2,
                              TreeNode(4,
                                       TreeNode(5))),
                     TreeNode(3)),
            False
        ),
        (
            "Test Case 4 - balanced",
            TreeNode(1,
                     TreeNode(2,
                              TreeNode(4),
                              TreeNode(5)),
                     TreeNode(3,
                              None,
                              TreeNode(6))),
            True
        )
    ]

    for name, tree, expected in test_cases:
        result = checkBalanced(tree)
        # Assertion to ensure expected outcome.
        assert result == expected, f"{name} failed: expected {expected}, got {result}"
        print(f"{name} passed!")

# Run all tests
run_tests()

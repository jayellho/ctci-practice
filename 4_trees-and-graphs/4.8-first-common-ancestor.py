'''
4.8 First Common Ancestor:
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree.
Avoid storing additional nodes in a data structure.
NOTE: This is not necessarily a binary search tree.
'''
# define classes.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# define functions.
res = [0]
def firstCommonAncestor(binTree, p, q):

    def dfs(node):

        # base case.
        if not node:
            return None
        # print(node.val)


        if node.val == p or node.val == q:
            return node.val

        # recurse.
        left = dfs(node.left)
        right = dfs(node.right)

        if left and right:
            return node.val
        if left:
            return left
        if right:
            return right

        




    # res = [0]

    res = dfs(binTree)
    print(f"ans = {res}")



# test cases.
## 1
binTree = TreeNode(10,
            left=TreeNode(5),
            right=TreeNode(15,
                        left=TreeNode(6),  # 6 is less than 10; violation!
                        right=TreeNode(20)))

firstCommonAncestor(binTree, 6, 15)
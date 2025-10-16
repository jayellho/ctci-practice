# Binary Tree Implementation
class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root


    # traversals =========================================================
    def in_order_traversal(self, node):

        if not node:
            return
        
        self.in_order_traversal(node.left)
        print(node.val)
        self.in_order_traversal(node.right)
    

    def post_order_traversal(self, node):
        if not node:
            return
        
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        print(node.val)
        
    def pre_order_traversal(self,node):
        if not node:
            return
        
        print(node.val)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)
        

    # search =============================================================

    def search_node(self, key, node=None):

        if not node:
            return
        
        if node.val == key:
            return node

        self.search_node(key, node.left)
        self.search_node(key, node.right)


# Driver code
if __name__ == "__main__":
    tree = BinaryTree(BinaryTreeNode(1))
    tree.root.left = BinaryTreeNode(2)
    tree.root.right = BinaryTreeNode(3)
    tree.root.left.left = BinaryTreeNode(4)
    tree.root.left.right = BinaryTreeNode(5)
    tree.root.right.left = BinaryTreeNode(6)
    tree.root.right.right = BinaryTreeNode(7)

    print("In-order Traversal:")
    tree.in_order_traversal(tree.root)
    print("Pre-order Traversal:")
    tree.pre_order_traversal(tree.root)
    print("Post-order Traversal:")
    tree.post_order_traversal(tree.root)
    result = tree.search_node(5, tree.root)
    if result:
        print(f"Node with value {result.val} found.")
    else:
        print("Node not found.")

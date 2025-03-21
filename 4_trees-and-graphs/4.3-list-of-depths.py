'''
4.3 List of Depths:
Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth
(e.g. if you have a tree with depth D, you'll have D linked lists).
'''

'''
- use a dictionary to store the linked lists at each depth.
- do a bfs traversal of the tree, and at each node, track the depth and add to the end of linked list.
    - use a queue, each item: (<node>, <depth>)
    - while loop not empty:
        - pop
        - check if depth exists in dict.
            - if not, create new k, v and set next val in linked list to current node.
            - else, set ll.next to curr node and move the ptr forward.

'''
# code.
import collections

class LinkedLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listOfDepths(bin_tree:TreeNode)->dict:
    # define vars.
    res = {}
    q = []
    
    # bfs over q.
    q.append((bin_tree, 0))

    while q:
        # bfs by level.
        next_level = []
        for node, depth in q:
            ## add current level nodes into dictionary of linked lists.
            if depth not in res:
                res[depth] = LinkedLNode(node.val)
                ptr = res[depth]
            else:
                ptr.next = LinkedLNode(node.val)
                ptr = ptr.next

            ## collect children.
            if node.left:
                next_level.append((node.left, depth+1))
            if node.right:
                next_level.append((node.right, depth+1))
        q = next_level

    return res


# test cases.
## 1
bin_tree = TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(6), right=TreeNode(7)), right=TreeNode(4)), right=TreeNode(5, left=TreeNode(8), right=TreeNode(9, left=TreeNode(10))))
llOfDepths = listOfDepths(bin_tree)

def printLLOfDepths(dict_of_ll):
    for k, v in dict_of_ll.items():
        nodes = []
        while v:
            nodes.append(v.val)
            v = v.next
        print(f"depth = {k}: nodes = {nodes}")

printLLOfDepths(llOfDepths)      
     
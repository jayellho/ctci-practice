'''
4.9 BST Sequences:
A binary search tree was created by traversing through an array from left to right and inserting each element.
Given a binary search tree with distinct elements, print all possible arrays that could have led to this tree.

EXAMPLE
Input:
        2
       / \
      1   3

Output: {2, 1, 3}, {2, 3, 1}
'''
import collections

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def weave(left, right, prefix, res):
    '''
    return: list of lists representing all possible weaves of the given left and right lists.
    '''
    if not right:
        tmp = prefix.copy()
        tmp.extend(left)
        res.append(tmp)
        return res
    if not left:
        tmp = prefix.copy()
        tmp.extend(right)
        res.append(tmp)
        return res

    prefix.append(left[0])
    weave(left[1:], right, prefix, res)
    prefix.pop()
    prefix.append(right[0])
    weave(left, right[1:], prefix, res)
    prefix.pop()
    return res

def bstSequences(node):
     
    # base case.
    if not node:
        return [[]]
     
    # iterate.
    prefix = [node.val]

    leftSeq = bstSequences(node.left)
    rightSeq = bstSequences(node.right)
    res = []
    for l in leftSeq:
        for r in rightSeq:
            weaved = []
            weave(l, r, prefix, weaved)
            res.extend(weaved)
    return res


# --- Test Cases ---

# Example 1: The balanced BST with nodes 1 through 7:
#         4
#       /   \
#      2     6
#     / \   / \
#    1   3 5   7
eg = Node(4,
          left=Node(2, left=Node(1), right=Node(3)),
          right=Node(6, left=Node(5), right=Node(7)))
seqs1 = bstSequences(eg)
print(seqs1)
# For a tree with 7 nodes:
#  - The left subtree (nodes 1,2,3) produces 2 sequences.
#  - The right subtree (nodes 5,6,7) produces 2 sequences.
#  - The number of ways to interleave two sequences of 3 elements each is binom(6, 3) = 20.
# Total expected sequences: 2 * 2 * 20 = 80.
assert len(seqs1) == 80, f"Expected 80 sequences for eg, got {len(seqs1)}"
# Also verify that each sequence starts with the root value, 4.
for seq in seqs1:
    assert seq[0] == 4, f"Sequence {seq} does not start with root 4."

# Example 2: Simple BST with 3 nodes:
#      2
#     / \
#    1   3
eg2 = Node(2, left=Node(1), right=Node(3))
seqs2 = bstSequences(eg2)
print(seqs2)
# For a tree with 3 nodes, the left and right subtrees each yield one sequence,
# and the interleaving of two lists of one element each gives binom(2,1) = 2 sequences.
assert len(seqs2) == 2, f"Expected 2 sequences for eg2, got {len(seqs2)}"
for seq in seqs2:
    assert seq[0] == 2, f"Sequence {seq} does not start with root 2."

# Example 3: BST with a single node
eg3 = Node(1)
seqs3 = bstSequences(eg3)
print(seqs3)
assert seqs3 == [[1]], f"Expected [[1]] for single-node tree, got {seqs3}"

# Example 4: Empty tree (None)
seqs4 = bstSequences(None)
print(seqs4)
assert seqs4 == [[]], f"Expected [[]] for empty tree, got {seqs4}"

print("All tests passed!")
'''
4.2 Minimal Tree:
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

'''

'''
[1, 2, 3, 4, 5, 6, 7]

- minimal ==> each level is maxed out ==> as balanced as possible.
-      4
    2     6
   1  3  5  7
'''

import collections


# define Node class.
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# define function.
def createMinimalTree(sorted_arr):

    def recurse(left, right):

        # base case.
        if right < left:
            return

        # do something with current node.
        mid = (left + right) // 2
        node = Node(sorted_arr[mid])

        # recurse.
        node.left = recurse(left, mid-1)
        node.right = recurse(mid+1, right)
        return node
    res = recurse(0, len(sorted_arr) - 1)

    return res


# create test cases.

## 1
sorted_arr = [1, 2, 3, 4, 5, 6]
tree = createMinimalTree(sorted_arr)

def print_tree(tree):
    q = collections.deque()

    q.append(tree)

    while q:
        curr = q.popleft()
        print(f"curr = {curr.data}")
        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)

print_tree(tree)




        
'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

def sum_left_leaves(root):
    if not root: return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sum_left_leaves(root.right)
    return sum_left_leaves(root.left) + sum_left_leaves(root.right)

from collections import deque
def sum_left_leaves_v2(root):
    que = deque([root])
    result = 0

    while que:
        current = que.popleft()
        if current.left and not current.left.left and not current.left.right:
            result += current.left.val 
        if current.left: que.append(current.left)
        if current.right: que.append(current.right)

    return result
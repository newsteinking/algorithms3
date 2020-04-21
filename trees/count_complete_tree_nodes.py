'''
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 /   /
4  5 6

Output: 6
'''

def count_nodes(root):
    def left_depth(root):
        if root is None: return 0
        return 1 + left_depth(root.left)

    def count(root):
        if root is None: return 0
        left = left_depth(root.left)
        right = left_depth(root.right)
        if left > right:
            return 2 ** right + count(root.left)
        else:
            return 2 ** left + count(root.right)

    return count(root)


def count_nodes_v2(root):
    if root is None: return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
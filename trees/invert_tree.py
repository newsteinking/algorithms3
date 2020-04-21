'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 /   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 /    / \
9   6 3   1
'''

def invert_tree(root):
    if root is None:
        return 
    else:  
        invert_tree(root.left)
        invert_tree(root.right)

        root.left, root.right = root.right, root.left
    return root

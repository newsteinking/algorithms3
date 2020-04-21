'''
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       /    
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''

def diameter_binary_tree(root):
    diameter = 1

    def depth(root):
        nonlocal diameter
        if root is None: return 0
        L = depth(root.left)
        R = depth(root.right)
        diameter = max(diameter, L + R + 1)
        return 1 + max(L, R)

    depth(root)
    return diameter - 1
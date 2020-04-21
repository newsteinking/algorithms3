'''
Given two binary trees, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical and the nodes
 have the same value.
Example 1:
Input:     1         1
          /         / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          /        / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
'''

def same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True 

    if root1 is not None and root2 is not None:
        if root1.val == root2.val and \
           same_tree(root1.left, root2.left) and \
           same_tree(root1.right, root2.right):
           return True
    return False 



'''
Given a tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   /      \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None 

def increasing_bst(root):

    def dfs(root):
        if root:
            dfs(root.left)
            root.left = None
            increasing_bst.cur.right = root 
            increasing_bst.cur = root 
            dfs(root.right)

    new_root = increasing_bst.cur = TreeNode(0)
    dfs(root)
    return new_root.right
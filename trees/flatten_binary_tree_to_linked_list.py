'''
en a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 /   \
3   4   6
The flattened tree should look like:

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
'''

def flatten(root):
    prev = None
        
    def dfs(root):
        nonlocal prev 
        if not root: return None
        
        dfs(root.right)
        dfs(root.left)
        
        root.right = prev
        root.left = None
        
        prev = root
    
    dfs(root)
    return 
        
'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to 
any node in the tree along the parent-child connections. The path must contain at least one 
node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null, null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

def max_path_sum(root):
    max_sum = float('-inf')

    def helper(root):
        if root is None: return 0
        nonlocal max_sum 
        
        left = helper(root.left)
        right = helper(root.right)

        max_at_root = max(root.val, root.val+left, root.val+right, root.val+left+right)
        if max_at_root > max_sum:
            max_sum = max_at_root

        return max(root.val, root.val+left, root.val+right)

    helper(root)
    return max_sum

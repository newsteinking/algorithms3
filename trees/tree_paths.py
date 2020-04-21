'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

def tree_paths(root):
    result, path = list(), list()

    def helper(root):
        if root is None:
            return 
        path.append(root.val)
        if not root.left and not root.right:
            result.append(path[:])
        if root.left: helper(root.left)
        if root.right: helper(root.right)

        path.pop()

    helper(root)
    return result

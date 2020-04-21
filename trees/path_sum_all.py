'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /     / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

def path_sums_all(root, target):
    result, path = list(), list()

    def helper(root, sum_so_far):
        if root is None:
            return

        path.append(root.val)
        sum_so_far += root.val
        
        if not root.left and not root.right and sum_so_far == target:
            result.append(path[:])

        if root.left: helper(root.left, sum_so_far)
        if root.right: helper(root.right, sum_so_far)

        path.pop()

    helper(root, 0)
    return result
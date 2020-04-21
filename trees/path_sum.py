'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the
 values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /        \
7    2      1

'''

def path_sum(root, target):
    if root is None:
        return target == 0
    else:
        ans = 0
        subSum = target - root.val

        if subSum == 0 and not root.left and not root.right:
            return True

        if root.left:
            ans = ans or path_sum(root.left, subSum)
        if root.right:
            ans = ans or path_sum(root.right, subSum)

        return ans



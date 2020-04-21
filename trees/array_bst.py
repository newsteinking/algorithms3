'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def array_bst(nums:list):
    if not nums: return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = array_bst(nums[:mid])
    root.right = array_bst(nums[mid+1:])
    return root

def array_bst_v2(nums):
    if not nums:
        return None

    def to_bst(left, right):
        if left > right:
            return None

        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = to_bst(left, mid-1)
        node.right = to_bst(mid+1, right)
        return node

    return to_bst(0, len(nums)-1)
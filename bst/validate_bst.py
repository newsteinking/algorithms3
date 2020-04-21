'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''

def is_valid_bst(root):
    prev = None

    def helper(root):
        nonlocal prev
        if not root: return True
        if not helper(root.left):
            return False
        if prev and prev.val >= root.val:
            return False
        prev = root
        return helper(root.right)

    return helper(root)

def is_valid_bst_v2(root):
    stack = []
    done = False
    current = root
    prev = None
    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if stack:
                current = stack.pop()
                if prev and prev.val >= current.val:
                    return False
                prev = current
                current = current.right
            else:
                done = True
    return True


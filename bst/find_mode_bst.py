'''

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) 
in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2
 

return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space 
incurred due to recursion does not count).
'''

def find_mode(root):

    def inorder(root):
        nonlocal prev, mode_length, current_length
        if root:
            inorder(root.left)
            if root.val != prev:
                prev = root.val
                current_length = 0
            current_length += 1
            mode_length = max(mode_length, current_length)
            inorder(root.right)

    def mode(root):
        nonlocal prev, count
        if root:
            mode(root.left)
            if root.val != prev:
                prev = root.val
                count = 0
            count += 1
            if count == mode_length: modes.append(root.val)
            mode(root.right)
    
    mode_length, current_length, prev = 0, 0, None
    inorder(root)

    prev, count, modes = None, 0, list()
    mode(root)

    return modes

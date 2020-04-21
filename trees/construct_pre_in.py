'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree_inpre(preorder, inorder):
    inorder_hash = {}
    for i, e in enumerate(inorder):
        inorder_hash[e] = i
    pre_index = [0]
    def build(start, end, inorder, preorder):
        if start > end:
            return None

        new_node = TreeNode(preorder[pre_index[0]])
        pre_index[0] += 1

        if start == end:
            return new_node

        index = inorder_hash[new_node.val]
        new_node.left = build(start, index-1, inorder, preorder)
        new_node.right = build(index+1, end, inorder, preorder)

        return new_node

    return build(0, len(inorder)-1, inorder, preorder)


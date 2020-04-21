'''Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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

def build_tree_postorder(inorder, postorder):
    inorder_hash = {}
    for i, e in enumerate(inorder):
        inorder_hash[e] = i
    post_index = [len(postorder)-1]

    def build(start, end, inorder, postorder):
        if start > end:
            return None

        new_node = TreeNode(postorder[post_index[0]])
        post_index[0] -= 1

        if start == end:
            return new_node

        index = inorder_hash[new_node.val]
        new_node.right = build(index+1, end, inorder, postorder)
        new_node.left = build(start, index-1, inorder, postorder)

        return new_node

    return build(0, len(inorder)-1, inorder, postorder)


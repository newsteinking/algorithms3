'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 /   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
     \
    4   7
'''

def delete_node(root, key):
        
    def inorder_succ(node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def helper(root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = helper(root.left, key)
        elif key > root.val:
            root.right = helper(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = inorder_succ(root.right)
            root.val = temp.val
            root.right = helper(root.right, temp.val)
        return root

    return helper(root, key)
'''
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
'''
try:
    from .bst_implementation import * 
except Exception: 
    from bst_implementation import *

def traverse(root,first, prev, last):
    if root:
        first, prev, last = traverse(root.left, first, prev, last)
        if prev and prev.val > root.val:
            if not first:
                first = prev
                last = root
            else:
                last = root
        prev = root
        first, prev, last = traverse(root.right, first, prev, last)
    return first, prev, last

def recover_tree(root) -> None:
    '''
    Nothing is returned. Tree is modified in place
    '''
    first, prev, last = None, None, None
    first, prev, last = traverse(root, first, prev, last)
    first.val, last.val = last.val, first.val



def recover_tree_v2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur, prev, drops, stack = root, bst.TreeNode(float('-inf')), [], []        
        while cur or stack:                                                    
            while cur:                                                         
                stack.append(cur)                                               
                cur = cur.left                                                 
            node = stack.pop()                                                
            if node.val < prev.val: drops.append((prev, node))                 
            prev, cur = node, node.right                                       
        drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val

def recover_tree_v3(root):
    def traverse(root, inorder):
        if root:
            traverse(root.left, inorder)
            inorder.append(root.val)
            traverse(root.right, inorder)
        return inorder

    def insert_bst_inorder(root, inorder):
        if root:
            insert_bst_inorder(root.left, inorder)
            root.val = inorder[0]
            inorder.pop(0)
            insert_bst_inorder(root.right, inorder)
    inorder = traverse(root, [])
    inorder.sort()
    insert_bst_inorder(root, inorder)

def recoverBST(root):
    first, second, prev = None, None, None

    def traverse(root):
        nonlocal first, second, prev
        if root:
            traverse(root.left)
            if prev and prev.val > root.val:
                if not first:
                    first = prev
                    second = root
                else:
                    second = root
            prev = root
            traverse(root.right)

    traverse(root)
    first.val, second.val = second.val, first.val




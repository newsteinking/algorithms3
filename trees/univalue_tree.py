'''
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
'''

def univalue_tree(root):
    if not root: return False
    
    unique = root.val 
    stack = [root]

    while stack:
        current = stack.pop()
        if current.val != unique:
            return False 
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)

    return True 
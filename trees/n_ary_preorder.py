'''
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:
Return its preorder traversal as: [1,3,5,6,2,4].
Note:

Recursive solution is trivial, could you do it iteratively?
'''

def n_ary_preorder(root):
    traversal = []
        
    def traverse(root):
        if root:
            traversal.append(root.val)
            for child in root.children:
                traverse(child)
    
    traverse(root)
    return traversal

def n_ary_preorder_iterative(root):
    stack, result = [], []
    if not root: return result
    stack.append(root)

    while stack:
        current = stack.pop()
        result.append(current.val)
        for child in current.children[::-1]:
            stack.append(child)

    return result 

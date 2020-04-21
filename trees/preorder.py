'''
Given a binary tree, return the preorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
'''

def preorder_recursive(root):
    result = []
    
    def helper(root):
        if root:
            result.append(root.val)
            helper(root.left)
            helper(root.right)
    
    helper(root)
    return ','.join(str(x) for x in result)

def preorder_iterative(root):
    if root == None:
        return ''
    stack = []
    stack.append(root)
    result = []
    while len(stack) > 0:
        temp = stack.pop()
        result.append(temp.val)
        if temp.right: stack.append(temp.right)
        if temp.left: stack.append(temp.left)
    return ','.join(str(x) for x in result)
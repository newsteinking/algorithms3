'''
Given a binary tree, return the inorder traversal of its nodes' value
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [1,3,2]
'''

def inorder_recursive(root):

    def helper(root):
        if root:
            helper(root.left)
            result.append(root.val)
            helper(root.right)
    
    result = []
    helper(root)
    return ','.join(str(x) for x in result)

def inorder_iterative(root):
    current = root
    stack = []
    done = False
    result = []
    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                result.append(current.val)
                current = current.right
            else:
                done = True
    return ','.join(str(x) for x in result)
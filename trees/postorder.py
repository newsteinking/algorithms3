'''
Given a binary tree, return the postorder traversal of its nodes' values.
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3
Output: [3,2,1]
'''

def postorder_recursive(root):
    result = []

    def helper(root):
        if root:
            helper(root.left)
            helper(root.right)
            result.append(root.val)

    helper(root)
    return ','.join(str(x) for x in result)

def postorder_iterative(root):
    stack1 = []
    stack2 = []

    stack1.append(root)

    while len(stack1) > 0:
        temp = stack1.pop()
        if temp.left: stack1.append(temp.left)
        if temp.right: stack1.append(temp.right)
        stack2.insert(0, temp.val)

    return ','.join(str(x) for x in stack2)


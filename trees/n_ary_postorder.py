'''
Given an n-ary tree, return the postorder traversal of its nodes' values.
For example, given a 3-ary tree:
Return its postorder traversal as: [5,6,3,2,4,1].
Note:
Recursive solution is trivial, could you do it iteratively?
'''

def n_ary_preorder(root):
    traversal = []
        
    def traverse(root):
        if root:
            for child in root.children:
                traverse(child)
            traversal.append(root.val)
    
    traverse(root)
    return traversal


def n_ary_postorder_iterative(root):
    if not root: return []
    stack1, stack2 = [root], []

    while stack1:
        temp = stack1.pop()
        for child in temp.children:
            stack1.append(child)
        stack2.append(temp.val)

    return stack2[::-1]

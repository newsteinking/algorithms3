'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is 
changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

def greater_tree(root):
    total = 0

    def inorder(root):
        nonlocal total
        if root: 
            inorder(root.right)
            total += root.val 
            root.val = total 
            inorder(root.left)

    inorder(root)
    return root 

def greater_tree_v2(root):

    def inorder(root):
        nonlocal sums 
        if root:
            inorder(root.left)
            sums.append(root.val)
            inorder(root.right)

    def update(root):
        nonlocal position, sums 
        if root:
            update(root.left)
            root.val = sums[position]
            position += 1
            update(root.right)

    sums, position = [], 0
    inorder(root)
    for i in range(len(sums) - 2, -1, -1):
        sums[i] += sums[i + 1]
    update(root)

    return root

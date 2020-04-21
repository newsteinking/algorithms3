'''
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number 
starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this 
could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
'''

def sum_root_to_leafs(root):
    parents, leafs = dict({root:None}), list()

    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            parents[node.left] = node
            stack.append(node.left)
        if node.right:
            parents[node.right] = node 
            stack.append(node.right)
        if not node.left and not node.right:
            leafs.append(node)

    result = 0
    for leaf in leafs:
        number = []
        while leaf:
            number.append(leaf.val)
            leaf = parents[leaf]
        result += int(''.join(str(x) for x in number[::-1]), 2)
        

    return result 


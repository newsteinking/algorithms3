'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
'''

from collections import deque
def are_cousins(root, x, y):
    parents = {root.val:None}
    que = deque([(root, 0)])
    node_x, node_y = None, None

    while que:
        node_count = len(que)
        for _ in range(node_count):
            current, level = que.popleft()
            if current.val == x: node_x = (current.val, level)
            if current.val == y: node_y = (current.val, level)

            if current.left:
                parents[current.left.val] = current.val
                que.append((current.left, level+1))
            if current.right:
                parents[current.right.val] = current.val
                que.append((current.right, level+1))

        if node_x and node_y: 
            break
   
    if node_x[1] == node_y[1] and parents[node_x[0]] != parents[node_y[0]]:
        return True
    else: return False 




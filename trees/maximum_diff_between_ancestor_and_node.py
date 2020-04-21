'''

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B 
where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

 

Example 1:



Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 

Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
'''

from collections import deque 

def max_ancestor_diff(root):
    parents, leafs = {root:None}, []
    
    def bfs(root):
        que = deque([root])
        while que:
            current = que.popleft()
            if current.left:
                que.append(current.left)
                parents[current.left] = current
            if current.right:
                que.append(current.right)
                parents[current.right] = current
            if current.left is None and current.right is None:
                leafs.append(current)

    bfs(root)
    max_diff = float('-inf')

    for leaf in leafs:
        min_node, max_node = float('inf'), float('-inf')
        p = leaf 
        while p:
            min_node = min(min_node, p.val)
            max_node = max(max_node, p.val)
            p = parents[p]
        max_diff = max(max_diff, abs(min_node - max_node))

    return max_diff 


'''
1123. Lowest Common Ancestor of Deepest Leaves
Medium

8

23

Favorite

Share
Given a rooted binary tree, find the lowest common ancestor of its deepest leaves.

Recall that:

The node of a binary tree is a leaf if and only if it has no children
The depth of the root of the tree is 0, and if the depth of a node is d, the depth of each of its children is d+1.
The lowest common ancestor of a set S of nodes is the node A with the largest depth such that every node in S is in the subtree with root A.
 

Example 1:

Input: root = [1,2,3]
Output: [1,2,3]
Example 2:

Input: root = [1,2,3,4]
Output: [4]
Example 3:

Input: root = [1,2,3,4,5]
Output: [2,4,5]
 

Constraints:

The given tree will have between 1 and 1000 nodes.
Each node of the tree will have a distinct value between 1 and 1000.
'''
from collections import deque 

def lca_deepest(root):
    que = deque([root])
    parents = {root:None}
    levels = []

    while que:
        count = len(que)
        level = []
        for _ in range(count):
            current = que.popleft()
            level.append(current)
            if current.left:
                que.append(current.left)
                parents[current.left] = current
            if current.right:
                que.append(current.right)
                parents[current.right] = current
        levels.append(level)

    levels = levels[-1]
    if len(levels) == 1: return levels[0]
    while True:
        for i in range(len(levels)):
            levels[i] = parents[levels[i]]
        if len(set(levels)) == 1: return levels[0]

    return -1    
'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the 
farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
'''
from collections import deque
def max_depth(root):
    if root is None:
        return 0
    else:
        lheight = max_depth(root.left)
        rheight = max_depth(root.right)

        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def max_depth_v2(root):
    if root is None:
        return 0

    que = deque()
    que.append(root)
    levels = 0
    nodecount = 1
    while len(que) > 0:
        while nodecount > 0:
            temp = que.popleft()
            if temp.left: que.append(temp.left)
            if temp.right: que.append(temp.right)
            nodecount -= 1
        nodecount = len(que)
        levels += 1
    return levels

def max_depth_v3(root):
    if root is None:
        return 0
    else:
        return 1 + max(max_depth_v3(root.left), max_depth_v3(root.right))



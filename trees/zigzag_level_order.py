'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. 
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
from collections import deque

def zigzag_level_order(root):
    if root is None:
        return []
    nodecount = 1
    que = deque()
    que.append(root)
    result = []
    odd = True
    while len(que) > 0:
        level = []
        while nodecount > 0:
            current = que.popleft()
            if current.left: que.append(current.left)
            if current.right: que.append(current.right)
            if odd:
                level.append(current.val)
            else:
                level.insert(0, current.val)
            nodecount -= 1
        nodecount = len(que)
        result.append(level)
        odd = not odd
    return result


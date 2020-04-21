'''
Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
from collections import deque

def level_order_one(root):
    if root is None:
        return []
    nodecount = 1
    que = deque()
    que.append(root)
    result = []
    while len(que) > 0:
        level = []
        while nodecount > 0:
            current = que.popleft()
            if current.left: que.append(current.left)
            if current.right: que.append(current.right)
            level.append(current.val)
            nodecount -= 1
        nodecount = len(que)
        result.append(level)
    return result


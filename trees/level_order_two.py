'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
from collections import deque

def level_order_two(root):
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
        result.insert(0, level)
    return result
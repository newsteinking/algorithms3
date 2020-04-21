'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down
 to the farthest leaf node.

For example, given a 3-ary tree:
'''
from collections import deque 

def max_depth_nary(root):
    if not root: return 0
    if not root.children: return 1
    return 1 + max(max_depth_nary(child) for child in root.children)

def max_depth_nary_bfs(root):
    if not root: return 0
    max_level = 1
    que = deque([(root, 1)])
    while que:
        current, level = que.popleft()
        max_level = max(level, max_level)
        for child in current.children:
            que.append((child, level + 1))

    return max_level

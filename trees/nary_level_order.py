'''
Given an n-ary tree, return the level order traversal of its nodes' 
values. (ie, from left to right, level by level).
For example, given a 3-ary tree
We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
'''
from collections import deque

def n_ary_level_order(root):
    que, seen, result = deque([root]), set(), list()

    while que:
        node_count = len(que)
        level = []
        for _ in range(node_count):
            current = que.popleft()
            level.append(current.val)
            seen.add(current)
            for node in current.children:
                if node not in seen:
                    que.append(node)
                    seen.add(node)
        result.append(level)

    return result 


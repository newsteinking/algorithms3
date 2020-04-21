'''
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
'''

from collections import deque

def find_bottom_left(root):
    max_level, left = 0, 0

    def dfs(root, level):
        nonlocal max_level, left
        if level > max_level:
            left = root.val 
            max_level = level 

        if root.left: dfs(root.left, level + 1)
        if root.right: dfs(root.right, level + 1)

    dfs(root, 1)
    return left

def find_bottom_left_v2(root):
    left = 0

    que = deque([root])
    while que:
        node_count = len(que)
        left = que[0].val 
        for _ in range(node_count):
            current = que.popleft()
            if current.left: que.append(current.left)
            if current.right: que.append(current.right)
    
    return left 

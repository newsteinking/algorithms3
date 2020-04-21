'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

from collections import deque

def min_depth(root):
    if root is None:
        return 0
    l = self.minDepth(root.left);
    r = self.minDepth(root.right);
    return l + r + 1 if l == 0 or r == 0 else min(l, r) + 1

def min_depth(root):
    if root is None:
        return 0
    que = deque()
    que.append(root)
    depth = 1
    while len(que) > 0:
        for _ in range(len(que)):
            current = que.popleft()
            if not current.left and not current.right:
                return depth
            if current.left: que.append(current.left)
            if current.right: que.append(current.right)
        depth += 1



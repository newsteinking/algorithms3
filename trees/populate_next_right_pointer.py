'''
You are given a perfect binary tree where all leaves are on the same 
level, and every parent has two children. The binary tree has the 
following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If 
there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.
'''

from collections import deque
def connect_next(root):
    que = deque([root])

    while que:
        current = que.popleft()
        if que:
            current.right = que[0]
        if current.left: que.append(current.left)
        if current.right: que.append(current.right)

    return root


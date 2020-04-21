'''
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   /   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  /      / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   /    
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   /     
  1   1
 /      
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.
'''
from collections import deque

class RowNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None 

def add_one_row(root, v, d):
    if d == 1:
        node = RowNode(v)
        node.left = root
        return node 

    def insert(root, depth):
        if depth == d - 1:
            root.left, root.left.left = RowNode(v), root.left
            root.right, root.right.right = RowNode(v), root.right
        else:
            if root.left and depth < d - 1: insert(root.left, depth + 1)
            if root.right and depth < d - 1: insert(root.right, depth + 1)

    insert(root, 1)
    return rootP

def add_one_row_v2(root, v: int, d: int):
    if d == 1:
        node = RowNode(v)
        node.left = root 
        return node 

    que = deque([root])
    level = 2
    while que:
        node_count = len(que)
        for _ in range(node_count):
            if level == d:
                current = que.popleft()
                current.left, current.left.left = RowNode(v), current.left
                current.right, current.right.right = RowNode(v), current.right
            else:
                current = que.popleft()
                if current.left: que.append(current.left)
                if current.right: que.append(current.right)
        if level == d: break
        level += 1

    return root 

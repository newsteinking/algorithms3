'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and 
node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's 
descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
'''
from collections import deque

def is_subtree(s, t):

    def equal(x, y):
        if x is None and y is None:
            return True 
        if x is None or y is None:
            return False 
        return x.val == y.val and equal(x.left, y.left) and equal(x.right, y.right)

    return s is not None and (equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
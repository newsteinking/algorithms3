'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
     \
  5     4       <---

'''
from collections import deque

def right_side(root) -> list:
    que = deque([root])
    result = list()

    while que:
        node_count = len(que)
        for i in range(len(que)):
            current = que.popleft()
            if i == node_count-1:
                result.append(current.data)
            if current.left: que.append(current.left)
            if current.right: que.append(current.right)

    return result

def right_side_v2(root):

    def helper(root, max_level, curr_level):
        if root is None:
            return

        if max_level[0] < curr_level:
            result.append(root.data)
            max_level[0] = curr_level

        helper(root.right, max_level, curr_level+1)
        helper(root.left, max_level, curr_level+1)

    max_level = [0]
    result = []
    helper(root, max_level, 1)
    return result

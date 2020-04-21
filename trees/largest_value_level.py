'''
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       /   
      5   3   9 

Output: [1, 3, 9]
'''

from collections import deque

def max_levels(root):
    if root is None:
        return []

    que = deque()
    que.append(root)
    result = []

    while len(que) > 0:
        maxx = float('-inf')
        for _ in range(len(que)):
            current = que.popleft()
            if current.val > maxx:
                maxx = current.val
            if current.left: que.append(current.left)
            if current.right: que.append(current.right)

        result.append(maxx)
    return result

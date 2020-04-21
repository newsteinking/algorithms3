'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 /  / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
      \
   3    3

'''

from collections import deque

def is_symmetric(root):

    def helper(root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is not None and root2 is not None:
            if root1.val == root2.val:
                return helper(root1.left, root2.right) and helper(root1.right, root2.left)

        return False

    return helper(root, root)

def is_symmetric_iterative(root):
    if root == None:
        return True

    if root.left is None and root.right is None:
        return True

    que = deque()
    que.append(root)
    que.append(root)
    left_node = 0
    right_node = 0

    while len(que) > 0:
        left_node = que.popleft()
        right_node = que.popleft()

        if left_node.val != right_node.val:
            return False

        if left_node.left and right_node.right:
            que.append(left_node.left)
            que.append(right_node.right)
        elif left_node.left or right_node.right:
            return False

        if left_node.right and right_node.left:
            que.append(left_node.right)
            que.append(right_node.left)
        elif left_node.right or right_node.left:
            return False

    return True


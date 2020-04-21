from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root == None:
            self.root = TreeNode(x)
            return
        
        que = deque()
        que.append(self.root)
        
        while len(que) > 0:
            temp =  que.popleft()
            if temp.left == None:
                temp.left = TreeNode(x)
                break
            
            if temp.right == None:
                temp.right = TreeNode(x)
                break

            que.append(temp.left)
            que.append(temp.right)

    def __repr__(self):
        if self.root == None:
            return ''
        result = []
        que = deque()
        que.append(self.root)

        while len(que) != 0:
            temp = que.popleft()
            result.append(temp.val)
            if temp.left: que.append(temp.left)
            if temp.right: que.append(temp.right)
        return ','.join(str(x) for x in result)

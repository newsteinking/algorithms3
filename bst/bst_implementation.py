from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def __repr__(self):
        result = []
        def inorder(root):
            if root:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        inorder(self.root)
        return ','.join(str(x) for x in result)

    def searchUtil(self, root, key):
        if root is None:
            return False
        if root.val == key:
            return True
        if root.val < key:
            return self.searchUtil(root.right, key)
        return self.searchUtil(root.left, key)

    def search(self, key):
        return self.searchUtil(self.root, key)
    
    def count(self):
        result = 0
        
        def countUtil(root):
            if root == None: return 0
            result = 0
            if root: result += 1
            if root.left: result += countUtil(root.left)
            if root.right: result += countUtil(root.right)
            return result
        
        return countUtil(self.root)

    def count_v2(self):
        self.count = 0
        
        def helper(root):
            if root:
                helper(root.left)
                self.count += 1
                helper(root.right)
        
        helper(self.root)
        return self.count

    def count_v3(self):
        if self.root == None:
            return 0
        count = 0
        que = deque()
        que.append(self.root)
        while len(que) != 0:
            temp = que.popleft()
            count += 1
            if temp.left: que.append(temp.left)
            if temp.right: que.append(temp.right)
        return count


    def insert_util(self, root, x):
        if root == None:
            root = TreeNode(x)
        else:
            if root.val < x:
                if root.right == None:
                    root.right = TreeNode(x)
                else:
                    self.insert_util(root.right, x)
            else:
                if root.left == None:
                    root.left = TreeNode(x)
                else:
                    self.insert_util(root.left, x)
        return root
        
    def insert_bst(self, x):
        self.root = self.insert_util(self.root, x)

    def get_max(self):
        if self.root == None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.val

    def get_min(self):
        if self.root == None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.val

    def get_height(self):
        
        def helper(node):
            if node is None:
                return 0
            else:
                left_height = helper(node.left)
                right_height = helper(node.right)

                if left_height > right_height:
                    return left_height + 1
                else:
                    return right_height + 1
        
        return helper(self.root)

    def delete_node(self, key):
        
        def inorder_succ(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        def helper(root, key):
            if root is None:
                return root
            if key < root.val:
                root.left = helper(root.left, key)
            elif key > root.val:
                root.right = helper(root.right, key)
            else:
                if root.left is None:
                    temp = root.right
                    root = None
                    return temp
                elif root.right is None:
                    temp = root.left
                    root = None
                    return temp
                temp = inorder_succ(root.right)
                root.val = temp.val
                root.right = helper(root.right, temp.val)
            return root

        self.root = helper(self.root, key)


'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two 
nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a 
descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]


 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to 
the LCA definition.
'''

def lowest_common_ancestor(root, p, q):
    parents = {root.val:None}
    seen_p = seen_q = False 
    stack = [root]

    while p not in parents or q not in parents:
        current = stack.pop()
        if current.left:
            parents[current.left.val] = current.val
            stack.append(current.left)
        if current.right:
            parents[current.right.val] = current.val
            stack.append(current.right)

    ancestors = set()

    while p:
        ancestors.add(p)
        p = parents[p]

    while q not in ancestors:
        q = parents[q]

    return q


def lowest_common_ancestor_v2(root, p, q):

    def dfs(root):
        nonlocal result
        if not root: return False 

        left = dfs(root.left)
        right = dfs(root.right)

        mid = root == p or root == q
        if mid + left + right >= 2:
            result = root 

        return mid or left or right 

    result = None    
    dfs(root)
    return result 


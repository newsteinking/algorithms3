'''
Consider all the leaves of a binary tree.  From left to right order, the values of 
those leaves form a leaf value sequence.



For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

def leaf_similar_tree(root1, root2):
    first_leafs, second_leafs = [], []

    def dfs(root, leafs):
        if not root: return
        if not root.left and not root.right:
            leafs.append(root.val)

        dfs(root.left, leafs)
        dfs(root.right, leafs)

    dfs(root1, first_leafs)
    dfs(root2, second_leafs)

    return first_leafs == second_leafs


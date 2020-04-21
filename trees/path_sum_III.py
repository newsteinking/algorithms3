'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   /     \
  3   2   11
 /   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''

def path_sum_three(root, sumx):
    paths = 0

    def inorder(root):
        nonlocal paths
        if root:
            inorder(root.left)
            dfs(root)
            inorder(root.right)

    def dfs(root):
        if root is None: return
        nonlocal sumx, paths 
        sumx -= root.val 

        if sumx == 0: paths += 1
        if root.left: dfs(root.left)
        if root.right: dfs(root.right)

        sumx += root.val 

    inorder(root)
    return paths
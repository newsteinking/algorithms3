'''
Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is 
defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). 
So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest 
frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
'''

def find_subree_sum(root):
    if not root: return []

    def dfs(root):
        if root is None: return 0
        left = dfs(root.left)
        right = dfs(root.right)
        sumx = root.val + left + right
        count[sumx] += 1

        return sumx

    count = Counter()
    dfs(root)
    max_value = max(count.values())
    return [x for x, c in count.items() if c == max_value]

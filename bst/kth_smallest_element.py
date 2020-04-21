'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest 
frequently? How would you optimize the kthSmallest routine?
'''

def kth_smallest_bst(root, k: int) -> int:
    kth_smallest = None
    
    def inorder(root):
        nonlocal kth_smallest, k
        if root:
            inorder(root.left)
            k -= 1
            if k == 0:
                kth_smallest = root.val
                return
            if k < 0: return 
            inorder(root.right)
    
    inorder(root)
    return kth_smallest
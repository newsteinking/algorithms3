'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

class XorTreeNode: 
    def __init__(self):
        self.left = None
        self.right = None

def insert(x, root):
    current = root
    for i in range(31, -1, -1):
        set_bit = (x >> i) & 1
        if set_bit:
            if current.right is None:
                current.right = XorTreeNode()
            current = current.right
        else:
            if current.left is None:
                current.left = XorTreeNode()
            current = current.left
    

def findMaximumXOR(self, A):
    max_xor = float('-inf')
    root = XorTreeNode()
    for val in A: insert(val, root)
    for val in A:
        current_xor = 0
        current = root
        for j in range(31, -1, -1):
            set_bit = (val >> j) & 1
            if set_bit:
                if current.left:
                    current_xor += 2**j
                    current = current.left
                else:
                    current = current.right
            else:
                if current.right:
                    current_xor += 2**j
                    current = current.right
                else:
                    current = current.left 
        max_xor = max(max_xor, current_xor)
    
    return max_xor 
    

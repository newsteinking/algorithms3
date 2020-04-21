'''
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always 
have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
'''

def has_alternating(n):
    odd, n = n & 1 != 0, n >> 1
    while n:
        even = n & 1 != 0
        if odd == even: return False 
        odd, n = even, n >> 1 
    
    return True 

def has_alternating_v2(n):
    return '00' not in bin(n) and '11' not in bin(n)


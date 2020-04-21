'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''

def power_of_two(n):
    if n == 1: return True 
    if n < 2: return False 
    
    multiple = 2
    while multiple <= n:
        if multiple == n:
            return True
        multiple *= 2
    return False 


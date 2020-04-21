'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, 
inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''

def bitwise_and_range(m, n):
    for i in range(32):
        m >>= 1
        n >>= 1
        if m == n: break

    return m << i 



'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = -2, b = 3
Output: 1
'''

def sum_two_numbers(a, b):
    if a == 0: return b
    if b == 0: return a

    mask = 0xffffffff

    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    return ~(a ^ mask) if (a >> 31) & 1 else a 

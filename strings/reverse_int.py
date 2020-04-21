'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
'''

def reverse_int(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0
    reverse = ''
    sign = -1 if x < 0 else 1
    x = abs(x)
    while x:
        reverse += str(x%10)
        x //= 10
    return sign*int(reverse) if (-(2**31)-1 < sign*int(reverse) < (2**31)) else 0

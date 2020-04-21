'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''

def to_base_7(num):
    if num == 0: return '0'
    sign = 1 if num < 0 else 0
    num = abs(num)

    result = []
    while num:
        digit = num % 7
        result.append(digit)
        num //= 7

    if sign: result.append('-')
    return ''.join(str(x) for x in result[::-1])
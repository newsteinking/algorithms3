'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''
from collections import deque
def add_binary(a, b):
    i = len(a)-1
    j = len(b)-1
    carry = 0
    result = deque()
    while i >= 0 or j >= 0:
        first = a[i] if i>=0 else 0
        second = b[j] if j>=0 else 0
        sumx = int(first) + int(second) + carry
        carry = sumx // 2
        sumx %= 2
        result.appendleft(sumx)
        i -= 1
        j -= 1
    if carry:
        result.appendleft(carry)
    return ''.join(str(x) for x in result)

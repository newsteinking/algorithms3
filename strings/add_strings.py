'''
Given two non-negative integers num1 and num2 represented as string, 
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs
 to integer directly.
'''
from collections import deque

def add_strings(num1, num2):
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    result = deque()

    while i >= 0 or j >= 0:
        num1_digit = int(num1[i]) if i >= 0 else 0
        num2_digit = int(num2[j]) if j >= 0 else 0

        sum_digit = num1_digit + num2_digit + carry 
        carry = sum_digit // 10
        sum_digit %= 10

        result.appendleft(str(sum_digit))
        i -= 1
        j -= 1

    if carry: result.appendleft(carry)
    return ''.join(result)


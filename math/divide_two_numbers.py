'''
Given two integers dividend and divisor, divide two integers without using 
multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume 
that your function returns 231 − 1 when the division result overflows.
'''

def divide_two_numbers(dividend, divisor):
    sign = -1 if ((dividend<0) ^ (divisor<0)) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    ans = 0

    while dividend >= divisor:
        dividend -= divisor
        ans += 1
        
    return sign * ans

def divide_two_numbers_v2(dividend, divisor):
    if divisor == 0: return -1 

    sign = 1 if ((dividend < 0) ^ (divisor < 0)) else 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    dividend_copy = dividend
    divisor_copy = divisor

    result, multiple = 0, 1

    while dividend_copy >= divisor:
        dividend_copy -= divisor_copy
        result += multiple
        multiple += multiple
        divisor_copy += divisor_copy
        if dividend_copy < divisor_copy:
            divisor_copy = divisor
            multiple = 1

    if sign: return max(-result, -2**31)
    else: return min(result, 2**31-1)

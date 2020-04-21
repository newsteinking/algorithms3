'''

Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:

Input: 3
Output: False
'''

def judge_square_sum(c):
    i = 0
    while i * i <= c:
        b = c - i * i
        left, right = 0, b
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == b: return True 
            if mid * mid < b:
                left = mid + 1
            else:
                right = mid - 1
        i += 1
    return False 


def judge_square_sum_v2(c):
    i = 0
    while i * i <= c:
        sq = math.sqrt(c - i * i)
        if sq == int(sq): return True 
        i += 1

    return False 

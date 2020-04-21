'''
Given a non-empty array of integers, return the third maximum number in 
this array. If it does not exist, return the maximum number. The time 
complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
'''

import heapq
def third_max_number(nums):
    nums = list(set(nums))
    if len(nums) < 3: return max(nums)
    heapq._heapify_max(nums)
    
    heapq._heappop_max(nums)
    heapq._heappop_max(nums)

    return heapq._heappop_max(nums)


'''
Given an integer array nums, find the contiguous subarray (containing 
at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
import sys
def maximum_subarray(nums):
    max_so_far, max_ending_here = -sys.maxsize-1, 0

    for number in nums:
        max_ending_here += number
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0: max_ending_here = 0

    return max_so_far
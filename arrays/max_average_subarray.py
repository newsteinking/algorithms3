'''
Given an array consisting of n integers, find the contiguous subarray of 
given length k that has the maximum average value. And you need to output 
the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
'''

def max_average_subarray(nums, k):
    max_sum = 0
    for i in range(k):
        max_sum += nums[i]

    curr_sum = max_sum
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i-k]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum / k


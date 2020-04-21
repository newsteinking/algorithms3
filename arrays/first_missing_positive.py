'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''

def first_missing_positive(nums):
    index = 0
    for i, val in enumerate(nums):
        if not 0 < val <= len(nums):
            nums[i], nums[index] = nums[index], nums[i]
            if nums[index] <= 0: nums[index] = 1
            index += 1
    
    for i in range(index, len(nums)):
        val = abs(nums[i])
        if nums[val - 1] > 0:
            nums[val - 1] = -nums[val - 1]
    
    for i in range(len(nums)):
        if nums[i] > 0:
            return i + 1

    return len(nums) + 1


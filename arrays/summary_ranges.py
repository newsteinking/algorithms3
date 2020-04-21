'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

def summary_ranges(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [str(nums[0])]

    start, end = 0, 1
    result = []
    
    while end < len(nums):
        while end < len(nums) and nums[end] - nums[end-1] <= 1:
            end += 1
        if nums[end-1] == nums[start]:
            result.append(str(nums[start]))
        else:
            result.append('->'.join([str(nums[start]), str(nums[end-1])]))
        
        start = end
        end += 1
        
    if start < len(nums):
        result.append(str(nums[start]))
    return result
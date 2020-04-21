'''
Given an array of size n, find the majority element. The majority element 
is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always 
exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

def majority_element(nums):
    if not nums: return 

    candidate = nums[0]
    count = 1

    for i in range(1, len(nums)):
        if nums[i] == candidate:
            count += 1
        elif nums[i] != candidate:
            count -= 1
        if count == 0:
            candidate = nums[i]
            count = 1

    return candidate

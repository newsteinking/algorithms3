'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

def search_range(nums, target):
    result = [-1, -1]

    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    if nums[left] != target:
        return result
    result[0] = left

    right = len(nums)-1
    while left < right:
        mid = (left + right) // 2 + 1
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid
    
    result[1] = right
    return result
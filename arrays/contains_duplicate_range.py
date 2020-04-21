'''
Given an array of integers and an integer k, find out whether 
there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

def contains_duplicate_range(nums, k):
    window = set()
    for index, number in enumerate(nums):
        if len(window) >= k+1:
            window.remove(nums[index-k-1])
        if number in window:
            return True 
        window.add(number)
    return False 




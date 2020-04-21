'''
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index 
is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should 
return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the 
right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
'''

def find_pivot_index(nums):
    S = sum(nums)
    leftsum = 0
    for i, x in enumerate(nums):
        if leftsum == (S - leftsum - x):
            return i
        leftsum += x
    return -1

def find_pivot_index_v2(nums):
    left, right = [0] * len(nums), [0] * len(nums)

    for i in range(1, len(nums)):
        left[i] = nums[i - 1] + left[i - 1]

    for i in range(len(nums) - 2, -1, - 1):
        right[i] = nums[i + 1] + right[i + 1]

    for i in range(len(left)):
        if left[i] == right[i]: return i 

    return -1


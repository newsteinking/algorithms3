'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

class NumArray:

    def __init__(self, nums):
        self.sums = [0] * (len(nums)+1)
        self.sums[0] = nums[0]
        for index in range(len(nums)):
            self.sums[index+1] = self.sums[index] + nums[index]

    def sum_range(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]



        


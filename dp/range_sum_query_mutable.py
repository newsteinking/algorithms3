'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''
import math
class NumArrayMutable:
    
    def __init__(self, nums):
        if not nums: return
        self.nums = nums
        self.bucket_width = int(math.sqrt(len(nums)))
        self.nb_buckets = (len(nums) // self.bucket_width) + 1
        self.bucket_sums = [0] * self.nb_buckets
        for i in range(len(nums)):
            self.bucket_sums[i // self.bucket_width] += nums[i]

    def update(self, i, val):
        self.bucket_sums[i // self.bucket_width] += (val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i, j):
        first = (i // self.bucket_width) + 1       # first full bucket
        last = (j // self.bucket_width) - 1        # last full bucket
        
        if first > last:    # sum directly from nums array
            return sum(self.nums[i:j+1])
            
        # else sum buckets
        result = sum(self.bucket_sums[first:last+1])
        # then add from i, to but excluding the first index of the first full bucket
        result += sum(self.nums[i:first * self.bucket_width])
        # then add from the first index of the bucket after the last full bucket, to but excluding j+1
        result += sum(self.nums[(last+1) * self.bucket_width:j+1])
        return result


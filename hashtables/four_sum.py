'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d 
in nums such that a + b + c + d = target? Find all unique quadruplets in the array which 
gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

from collections import defaultdict
def four_sum(nums, target):
    result = set()
    addition = defaultdict(list)
    for i in range(len(nums)-1):
        for j in range(1, len(nums)):
            sumx = target - nums[i] - nums[j]
            if sumx in addition:
                for t in addition[sumx]:
                    x = set([i, j, t[0], t[1]])
                    if len(x) == 4:
                        temp = sorted([nums[i], nums[j], nums[t[0]], nums[t[1]]])
                        temp = tuple(temp)
                        result.add(temp)
            addition[nums[i]+nums[j]].append([i, j])

    return list(result)


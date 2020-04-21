'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

def three_sum(nums):
    nums.sort()
    result = []
    seen = set()
    for i in range(len(nums)):
        start = i+1
        end = len(nums)-1

        while start < end:
            sumx = nums[i] + nums[start] + nums[end]
            if sumx == 0:
                if (nums[i], nums[start], nums[end]) not in seen:
                    result.append([nums[i], nums[start], nums[end]])
                    seen.add((nums[i], nums[start], nums[end]))
                start += 1
                end -= 1
                continue
            elif sumx < 0:
                start += 1
            else:
                end -= 1
    return result

def three_sum_v2(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)

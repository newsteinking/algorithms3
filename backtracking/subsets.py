'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

def subsets(nums:list) -> list:
    result = []

    def backtrack(temp, start):
        result.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            backtrack(temp, i+1)
            temp.pop()

    backtrack([], 0)
    return result

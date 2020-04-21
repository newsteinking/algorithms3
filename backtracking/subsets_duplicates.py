'''
Given a collection of integers that might contain duplicates, nums, return all 
possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

def subsets_duplicates(nums):
    result = []
    nums.sort()

    def backtrack(temp, start):
        result.append(temp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            backtrack(temp, i+1)
            temp.pop()

    backtrack([], 0)
    return result


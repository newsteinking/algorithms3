'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]'''

def permute(nums) -> list:
    result = []

    def backtrack(temp):
        if len(temp) == len(nums):
            result.append(temp[:])
        else:
            for i in range(len(nums)):
                if nums[i] in temp: continue
                temp.append(nums[i])
                backtrack(temp)
                temp.pop()

    backtrack([])
    return result

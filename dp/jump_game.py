'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''

from collections import defaultdict 

def can_jump(nums):
    last = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= last:
            last = i 
    return last == 0

def can_jump_v2(nums):
    memo = defaultdict(lambda: 'UNKNOWN')
    memo[len(nums) - 1] = 'GOOD'

    def backtrack(position):
        if memo[position] != 'UNKNOWN':
            return memo[position] == 'GOOD'

        jump = min(position + nums[position], len(nums) - 1)
        for i in range(position + 1, jump + 1):
            if backtrack(i):
                memo[position] = 'GOOD' 
                return True 

        memo[position] = 'BAD'
        return False 

    return backtrack(0)

def can_jump_v3(nums):

    def backtrack(position):
        if position == len(nums) - 1: return True 
        jump = min(position + nums[position], len(nums) - 1)
        for i in range(position + 1, jump + 1):
            if backtrack(i): return True 
        return False 

    return backtrack(0)

def can_jump_v4(nums):
    memo = defaultdict(lambda: 'UNKNOWN')
    memo[len(nums) - 1] = 'GOOD'

    for i in range(len(nums) - 1, -1, -1):
        jump = min(position + nums[position], len(nums) - 1)
        for j in range(i + 1, jump + 1):
            if memo[j] == 'GOOD':
                memo[i] = 'GOOD' 
                break  

    return memo[0] == 'GOOD'

def can_jump_v5(nums):
    dp = [True] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            dp[i] = dp[j] and nums[j] >= i-j
    return dp[-1]


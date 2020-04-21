'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

def can_partition(nums):
    
    def helper(start, target):
        if (start, target) in memo:
            return memo[(start, target)]
        if target < 0:
            return False 
        elif target == 0:
            return True 
        for i in range(start, len(nums)):
            if helper(i + 1, target - nums[i]):
                return True 
        memo[(start, target)] = False 
        return False 

    nums.sort()
    s = sum(nums)
    if s % 2: return False
    s = s / 2
    memo = {}
    return helper(0, s)

def can_partition_v2(nums):
    sumx = sum(nums)
    if sumx % 2: return False 
    dp = [[True for i in range(len(nums) + 1)] for j in range(sumx // 2 + 1)]
    for i in range(1, sumx // 2 + 1): dp[i][0] = False 

    for i in range(1, sumx // 2 + 1):
        for j in range(1, len(nums) + 1):
            dp[i][j] = dp[i][j - 1]
            if i >= nums[j - 1]:
                dp[i][j] = dp[i][j] or dp[i - nums[j -1]][j - 1]

    return dp[-1][-1]
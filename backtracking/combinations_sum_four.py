'''

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.


'''
import collections

def combinations_sum_four(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[-1]

def combinations_sum_four_v3(nums, target):

    def backtrack(remain = target):
        if remain in memo: return memo[remain]
        if remain < 0: return 0
        if remain == 0: return 1

        res = 0
        for i in range(len(nums)):
            res += backtrack(remain - nums[i])
        memo[remain] = res 
        return res
    
    memo = collections.defaultdict(int)
    res = backtrack()
    return res


def combinations_sum_four_v2(nums, target):
    result = 0

    def backtrack(remain):
        nonlocal result
        if remain < 0: return 
        if remain == 0: 
            result += 1
            return 
        for i in range(len(nums)):
            backtrack(remain - nums[i])

    backtrack(target)
    return result 

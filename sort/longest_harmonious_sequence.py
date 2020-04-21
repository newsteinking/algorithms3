'''
We define a harmonious array is an array where the difference between its maximum value and its minimum 
value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all 
its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
'''

from collections import Counter

def find_lhs(nums):
    count = Counter(nums)
        
    lhs = 0
    for x in count:
        if x + 1 in count:
            lhs = max(lhs, count[x] + count[x + 1])
    
    return lhs

def find_lhs_v2(nums) -> int:
    count = Counter(nums)
    nums = sorted(count.items(), key = lambda pair: pair[0])
    lhs = 0
    for i in range(1, len(nums)):
        if nums[i][0] - nums[i - 1][0] == 1:
            lhs = max(lhs, nums[i][1] + nums[i - 1][1])
    
    return lhs
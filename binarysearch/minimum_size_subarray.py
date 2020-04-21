'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous 
subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is 
O(n log n). 
'''

def min_subarray_sum(s, nums):
    result = len(nums) + 1
    sums = [0] * (len(nums))

    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]

    def find_left(left, right, val):
        while left < right:
            mid = (left + right) // 2
            if val - nums[mid] >= s:
                left = mid + 1
            else:
                right = mid 
        return left 

    left = 0
    for right, val in enumerate(nums):
        if val >= s:
            left = find_left(left, right, val)
            result = min(result, right - left + 1)

    return result if result <= len(nums) else 0



def min_subarray_sum_v2(s, nums):
    if not nums: return 0
    min_length = float('inf')
    sums = [0] * len(nums)
    sums[0] = nums[0] 

    for i in range(1, len(nums)):
        sums[i] = sums[i - 1] + nums[i]

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sumx = sums[j] - sums[i] + nums[i]
            if sumx >= s:
                min_length = min(min_length, j - i + 1)

    return min_length if min_length != float('inf') else 0

def min_subarray_sum_v3(s, nums):
    min_length = len(nums)

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sumx = sum(nums[i:j + 1])
            if sumx >= s:
                min_length = min(min_length, j - i + 1)

    return min_length 


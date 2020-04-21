'''
Given an unsorted array of integers, find the length of longest continuous increasing 
subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 
are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
'''

# def lis_continuous(nums):
# #     if not nums: return 0
# #
# #     longest_s = current_s = 1
# #     for i in range(len(nums) - 1):
# #         if nums[i] < nums[i + 1]:
# #             current_s += 1
# #         else:
# #             if current_s > longest_s:
# #                 longest_s = current_s
# #             current_s = 1
# #
# #     if current_s > longest_s: return current_s
# #     return longest_s
def longest_continuous_increasing_subsequence(nums):
    if not nums: return 0

    longest_s = current_s = 1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            current_s += 1
        else:
            if current_s > longest_s:
                longest_s = current_s
            current_s = 1

    if current_s > longest_s: return current_s
    return longest_s

'''
Given an integer array, you need to find one continuous subarray that if you only sort this 
subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted 
in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''

def shortest_unsorted_subarray(nums):
    if not nums: return 0
    left = 0
    while left < len(nums) - 1:
        if nums[left + 1] < nums[left]:
            break
        left += 1

    right = len(nums) - 1

    while right > 0:
        if nums[right - 1] > nums[right]:
            break
        right -= 1

    if right - left + 1 > 0:
        minx = min(nums[left:right+1])
        maxx = max(nums[left:right+1])

        while left > 0 and minx < nums[left-1]:
            left -= 1

        while right < len(nums) - 1 and maxx > nums[right+1]:
            right += 1
        
    return 0 if right - left <= 0 else right - left + 1
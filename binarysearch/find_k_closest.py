'''
Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
'''

from bisect import bisect_left

def find_k_closest(nums, k, x):
    if x > nums[-1]: return nums[:k:-1]
    if x < nums[0]: return nums[:k]
    index = bisect_left(nums, x)
    left, right = max(0, index-k-1), min(len(nums)-1, index+k-1)
    while right - left > k - 1:
        if left < 0 or x - nums[left] <= nums[right] - x:
            right -= 1
        elif right > len(nums)-1 or x - nums[left] > nums[right] - x:
            left += 1
    return nums[left:right+1]


def find_k_closest_v2(nums, k, x):
    left, right = 0, len(nums)-k
    while left < right:
        mid = (left + right) // 2
        if x - nums[mid] > nums[mid+k] - x:
            left = mid + 1
        else:
            right = mid
    return nums[left:left+k]


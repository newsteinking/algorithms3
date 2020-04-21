'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

def intersection_arrays(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    result = []
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    for number in nums1:
        if number in nums2:
            result.append(number)

    return result




'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both 
arrays.
The result can be in any order.
Follow up:
'''
from collections import Counter
def intersect_array(nums1, nums2):
    count = Counter(nums1)
    result = []

    for number in nums2:
        if number in count and count[number] > 0:
            result.append(number)
            count[number] -= 1
    
    result.sort()
    return result

def intersect_array_v2(nums1, nums2):
    count1 = Counter(nums1)
    count2 = Counter(nums2)
    result = []

    for element in count1:
        if element in count2:
            result += min(count1[element], count2[element]) * [element]
    return result

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

def majority_element_2(nums):
    count_1 = count_2 = 0
    majority_1 = majority_2 = None

    for num in nums:
        if num == majority_1:
            count_1 += 1
        elif num == majority_2:
            count_2 += 1
        elif count_1 == 0:
            majority_1 = num 
            count_1 = 1
        elif count_2 == 0:
            majority_2 = num
            count_2 = 1 
        else:
            count_1 -= 1 
            count_2 -= 1

    result = []
    count_1, count_2 = 0, 0
    for num in nums:
        if num == majority_1: count_1 += 1
        if num == majority_2: count_2 += 1

    if count_1 > len(nums) / 3: result.append(majority_1)
    if count_2 > len(nums) / 3: result.append(majority_2)

    return result 
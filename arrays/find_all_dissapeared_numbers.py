'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume 
the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
def find_all_disappeared_number(nums):
    result = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] > 0:
            nums[index] = - nums[index]

    for i in range(len(nums)):
        if nums[i] > 0:
            result.append(i+1)

    return result

# def find_disappeared(nums):
#     result = []
#     for i in range(len(nums)):
#         index = abs(nums[i]) - 1
#         if nums[index] > 0:
#             nums[index] = - nums[index]
#
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             result.append(i+1)
#
#     return result
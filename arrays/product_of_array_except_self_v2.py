'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is 
equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra 
space for the purpose of space complexity analysis.)
'''

# def product_of_array_except_self(nums):
#     result = [1] * len(nums)
#     for i in range(len(nums) - 2, -1, -1):
#         result[i] = result[i + 1] * nums[i + 1]
#
#     product = nums[0]
#     for i in range(1, len(nums)):
#         result[i] *= product
#         product *= nums[i]
#
#     return result
    
def product_of_array_except_self_v2(nums):
    left = [1] * len(nums)
    right = [1] * len(nums)

    for i in range(1, len(nums)):
        left[i] = left[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        right[i] = right[i + 1] * nums[i + 1]

    output = [1] * len(nums)
    for i in range(len(nums)):
        output[i] = left[i] * right[i]

    return output


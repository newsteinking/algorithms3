'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements 
appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space 
complexity?
'''

def single_number_three(nums):
    xor = 0
    for num in nums:
        xor ^= num 

    position = 0
    while xor:
        if xor & 1: break
        xor >>= 1
        position += 1

    mask = 1 << position
    unique_1 = unique_2 = 0
    for num in nums:
        if num & mask:
            unique_1 ^= num 
        else:
            unique_2 ^= num 

    return [unique_1, unique_2]

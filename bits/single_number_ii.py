'''
Given a non-empty array of integers, every element appears three times except for one, which appears 
exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra 
memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

def single_number_twice(nums):
    result = 0
    for i in range(32):
        sumx = 0
        x = (1 << i)
        for j in range(len(nums)):
            if nums[j] & x:
                sumx += 1
        if sumx % 3: result |= x
    if result >= 2**31: result -= 2**32
    return result 

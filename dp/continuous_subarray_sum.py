'''
Given a list of non-negative numbers and a target integer k, write a function to check if the 
array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, 
sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''


def subarray_sum(nums, k):
    if len(nums) < 2: return False 

    for i in range(len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] == 0: return True 

    if k == 0: return False 
    if k < 0: k = -k 

    sumx = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        sumx[i] = sumx[i - 1] + nums[i - 1]

    for i in range(len(nums)):
        for j in range(i + 2, len(nums) + 1):
            if (sumx[j] - sumx[i]) % k == 0: 
                return True 

    return False 


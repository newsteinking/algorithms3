'''
Given an array consists of non-negative integers, your task is to count the number of triplets 
chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''

def valid_triangle_number(nums):
    count = 0
    nums.sort()
    for i in range(len(nums) - 2):
        k = i + 2
        for j in range(i + 1, len(nums) - 1):
            if nums[i] == 0: break
            while k < len(nums) and nums[i] + nums[j] > nums[k]:
                k += 1
            count += k - j - 1
    return count

def valid_triangle_number_v2(nums):
    count = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j] > nums[k] and 
                    nums[i] + nums[k] > nums[j] and 
                    nums[j] + nums[k] > nums[i]):
                    count += 1

    return count 


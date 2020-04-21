'''
Given a binary array, find the maximum number of consecutive 1s in 
this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are 
consecutive 1s.
The maximum number of consecutive 1s is 3.

'''

def max_consecutive_ones(nums):
    max_so_far, max_current = 0, 0

    for digit in nums:
        if digit == 0:
            if max_current > max_so_far:
                max_so_far = max_current
            max_current = 0
        else:
            max_current += 1

    return max(max_so_far, max_current)



'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''

def contiguous_array(nums):
    count, count_hash = 0, {0: -1}
    max_size = 0

    for index, num in enumerate(nums):
        count += 1 if num else -1

        if count in count_hash:
            max_size = max(max_size, index - count_hash[count])
        else:
            count_hash[count] = index

    return max_size


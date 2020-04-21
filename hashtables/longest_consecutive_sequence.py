'''

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

def longest_consecutive(nums):
    numbers = set(nums)
    max_len = 0

    for num in nums:
        if num - 1 not in numbers:
            next_num = num + 1
            while next_num in numbers:
                next_num += 1
            max_len = max(max_len, next_num - num)

    return max_len


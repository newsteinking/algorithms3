'''
Given a non-empty integer array of size n, find the minimum number of moves required to 
make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
'''

# def minimum_moves(nums):
#     nums.sort()
#
#     count = 0
#     for i in range(len(nums)-1, -1, -1):
#         if nums[i] == nums[0]:
#             break
#         count += nums[i] - nums[0]
#
#     return count

def minimum_moves_to_equal_array(nums):
    nums.sort()

    count = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == nums[0]:
            break
        count += nums[i] - nums[0]

    return count
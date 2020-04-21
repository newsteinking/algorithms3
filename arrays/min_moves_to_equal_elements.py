'''
Given a non-empty integer array, find the minimum number of moves required to make 
all array elements equal, where a move is incrementing a selected element by 1 or 
decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''
def min_moves_to_equal_elements(nums):
    nums.sort()
    mid = len(nums) // 2
    median = nums[mid] if len(nums) % 2 else min(nums[mid - 1], nums[mid])

    moves = 0
    for val in nums:
        moves += abs(median - val)

    return moves
# def min_moves_2(nums):
#     nums.sort()
#     mid = len(nums) // 2
#     median = nums[mid] if len(nums) % 2 else min(nums[mid - 1], nums[mid])
#
#     moves = 0
#     for val in nums:
#         moves += abs(median - val)
#
#     return moves
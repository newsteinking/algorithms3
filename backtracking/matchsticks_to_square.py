'''
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the 
little match girl has, please find out a way you can make one square by using up all those 
matchsticks. You should not break any stick, but you can link them up, and each matchstick 
must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. 
Your output will either be true or false, to represent whether you could make one square 
using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
'''

def make_square(nums):
    sum_nums = sum(nums)
    if sum_nums % 4 != 0: return False 
    target = sum_nums // 4

    sums = [0]*4
    nums.sort(reverse=True)

    def backtrack(index=0, side=0):
        if sums[side] + nums[index] > target:
            return False 
        if index == len(nums)-1: return True 

        sums[side] += nums[index]
        for i in range(4):
            if backtrack(index+1, i):
                return True 
        sums[side] -= nums[index]
        return False 

    return backtrack()


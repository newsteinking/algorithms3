'''
Given an array nums of n integers and an integer target, find three integers in nums 
such that the sum is closest to target. Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

def three_sum_closest(nums:list, target: int) -> int:
    diff = float('inf')
    result = None
    nums.sort()
    
    for k in range(len(nums)-2):
        if k > 0 and nums[k] == nums[k - 1]:
            continue
        i, j = k+1, len(nums)-1
        while i < j:
            triplet = nums[k] + nums[i] + nums[j]
            if triplet == target:
                return triplet
            
            if abs(target-triplet) < diff:
                result = triplet
                diff = abs(target - triplet)
            elif triplet > target:
                j -= 1
            else:
                i += 1
    
    return result

def three_sum_closest_v2(nums, target):
    closest = [float('inf')]
    result = [0]
    nums.sort()

    def backtrack(temp, used):
        if len(temp) == 3:
            #print('helle')
            triplet = sum(temp)
            if abs(target - triplet) < closest[0]:
                #print('bye')
                closest[0] = target - triplet
                result[0] = triplet
        else:
            for i in range(len(nums)):
                if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                temp.append(nums[i])
                backtrack(temp, used)
                used[i] = False
                temp.pop()

    used = [False]*len(nums)        
    backtrack([], used)
    return result[0]

'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

def permute_unique(nums:list) -> list:
    result = set()

    def backtrack(so_far, rest):
        if len(rest) == 0:
            result.add(tuple(so_far))
        else:
            for i in range(len(rest)):
                next = so_far + [rest[i]]
                remain = rest[:i] + rest[i+1:]
                backtrack(next, remain)

    backtrack([], nums)
    return [list(x) for x in result]


def permute_unique_v2(nums):
    result = []
    nums.sort()
    def backtrack(temp, used):
        if len(temp) == len(nums):
            result.append(temp[:])
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
    return result

'''
Implement next permutation, which rearranges numbers into the 
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the 
lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its 
corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

def next_permutation(nums):
    found = False
    for i in range(len(nums)-1, 0, -1):
        if nums[i] > nums[i-1]:
            found = True
            break
    
    if not found:
        nums.reverse()
        return nums

    index = i
    for j in range(i+1, len(nums)):
        if nums[j] > nums[i-1] and nums[j] < nums[index]:
            index = j

    nums[i-1], nums[index] = nums[index], nums[i-1]
    nums[i:] = sorted(nums[i:])
    return nums

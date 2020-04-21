import sys

def selection_sort(nums):
    '''
    Takes an array of numbers and returns the sorted array 
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]: min_index = j 

        nums[min_index], nums[i] = nums[i], nums[min_index]

    return nums 



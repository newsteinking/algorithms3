def bubble_sort(nums:list) -> list:
    '''
    returns sorted list
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    '''
    for i in range(len(nums) - 1):
        swapped = False 
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped: break
        
    return nums 




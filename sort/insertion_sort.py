def insertion_sort(nums):
    '''
    returns sorted list
    '''
    for i in range(1, len(nums)):
        value = nums[i] 
        
        for j in range(i - 1, -1, -1):
            if nums[j] > value:
                nums[j + 1] = nums[j]
            else: break
        
        nums[j] = value

    return nums 
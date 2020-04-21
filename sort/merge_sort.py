def merge_sort(nums):
    '''
    sort list inplace
    return nothing
    '''
    if len(nums) < 2: return
    mid = len(nums) // 2
    L, R = nums[:mid], nums[mid:]
    
    merge_sort(L)
    merge_sort(R)
    
    i, j, k = 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1

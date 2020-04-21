'''
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

def trap_water(arr):
    next_greater = arr.copy()
    greatest = arr[-1]
    next_greater[-1] = -1
    for i in range(len(arr) - 2, -1, -1):
        next_greater[i] = greatest
        greatest = max(greatest, arr[i])
        if next_greater[i] <= arr[i]: next_greater[i] = -1

    prev_greater = arr.copy()
    greatest = arr[0]
    prev_greater[0] = -1
    for i in range(1, len(arr)):
        prev_greater[i] = greatest
        greatest = max(greatest, arr[i])
        if prev_greater[i] <= arr[i]: prev_greater[i] = -1

    water = 0
    for i in range(len(arr)):
        if next_greater[i] != -1 and prev_greater[i] != -1:
            water += min(next_greater[i], prev_greater[i]) - arr[i]

    return water

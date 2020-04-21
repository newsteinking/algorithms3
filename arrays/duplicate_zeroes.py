'''
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting 
the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your 
function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
'''

def duplicate_zeroes(arr):
    zero_count = arr.count(0)
    end = len(arr) - 1
    arr.extend([None] * zero_count)

    current = len(arr) - 1
    while end >= 0:
        if arr[end] == 0:
            arr[current] = 0
            current -= 1
            arr[current] = 0
            current -= 1
        else:
            arr[current] = arr[end]
            current -= 1
        end -= 1
    
    while zero_count:
        arr.pop()
        zero_count -= 1
    
    return arr 
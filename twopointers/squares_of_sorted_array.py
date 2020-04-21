'''
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''

def sorted_squares(A):
    i, j = 0, 0
    while j < len(A) and A[j] < 0: 
        j += 1
    
    i, j = j, j - 1
    result = []
    while i < len(A) and j > -1:
        if A[i] ** 2 > A[j] ** 2:
            result.append(A[j] ** 2)
            j -= 1
        else:
            result.append(A[i] ** 2)
            i += 1

    while i < len(A):
        result.append(A[i] ** 2)
        i += 1

    while j > -1:
        result.append(A[j] ** 2)
        j -= 1

    return result 

def sorted_squares_v2(A):
    return sorted(x*x for x in A)
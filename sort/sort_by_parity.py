'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, 
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''

def sort_array_parity(A):
    left, right = 0, len(A) - 1

    while left < right:
        while left < len(A) and not A[left] % 2: left += 1
        while right > -1 and A[right] % 2: right -= 1
        
        if left < right: A[left], A[right] = A[right], A[left]

    return A 

def sort_array_parity_v2(A):
    return sorted(A, key = lambda x: x % 2)
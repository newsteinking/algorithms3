'''
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... 
A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that 
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
'''

def mountain_array(A):
    if len(A) < 3: return -1
    left, right = 0, len(A) - 1

    while left + 1 < right:
        mid = (left + right) // 2
        if A[mid - 1] < A[mid] > A[mid + 1]:
            return mid 
        elif A[mid - 1] < A[mid] < A[mid + 1]:
            left = mid
        else:
            right = mid

    if 0 < left < len(A) - 1 and A[left - 1] < A[left] > A[left + 1]: 
        return left
    if 0 < right < len(A) - 1 and A[right - 1] < A[right] > A[right + 1]: 
        return right

    return -1 


'''

Given an array A of non-negative integers, return the maximum sum of elements in two 
non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, 
the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + 
A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.
 

Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.
 

Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
'''

def max_sum_two_subarrays(A, L, M):
    prefix_sum = [A[0]]
    for i in range(1, len(A)):
        prefix_sum.append(prefix_sum[-1] + A[i])

    max_sum = prefix_sum[L + M - 1]
    l_max = prefix_sum[L - 1]
    m_max = prefix_sum[M - 1]

    for i in range(L + M, len(A)):
        l_max = max(l_max, prefix_sum[i - M] - prefix_sum[i - M - L])
        m_max = max(m_max, prefix_sum[i - L] - prefix_sum[i - L - M])
        max_sum = max(max_sum, max(prefix_sum[i] - prefix_sum[i - M] + l_max, 
                                   prefix_sum[i] - prefix_sum[i - L] + m_max))

    return max_sum

def max_sum_two_subarrays_v2(A, L, M):
    prefix_sum = [0]
    for i in range(len(A)):
        prefix_sum.append(prefix_sum[-1] + A[i])

    max_sum = float('-inf')
    for i in range(L - 1, len(A)):
        for j in range(M - 1, len(A)):
            l = (i - L + 1, i)
            m = (j - M + 1, j)
            if max(l[0], m[0]) <= min(l[1], m[1]):
                continue
            sum_subarrray = prefix_sum[l[1] + 1] - prefix_sum[l[0]] + prefix_sum[m[1] + 1] - prefix_sum[m[0]]
            max_sum = max(max_sum, sum_subarrray)

    return max_sum


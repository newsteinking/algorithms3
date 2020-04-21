'''
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number
 (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:

Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is 
divisible by 5, so answer[0] is true.
Example 2:

Input: [1,1,1]
Output: [false,false,false]
Example 3:

Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]
Example 4:

Input: [1,1,1,0,1]
Output: [false,false,false,false,false]
'''

def prefix_divisible(A):
    for i in range(1, len(A)):
        A[i] += A[i - 1] * 2 % 5
    return [x % 5 == 0 for x in A]

def prefix_divisible_v2(A):
    result = []
    num = 0
    for i in range(len(A)):
        num = (num * 2 + A[i]) % 5
        result.append(num == 0)
    return result  

def prefix_divisible_v3(A):
    prefix, result = '', []
    for i in range(len(A)):
        prefix += str(A[i])
        result.append(False) if int(prefix, 2) % 5 else result.append(True)
    return result

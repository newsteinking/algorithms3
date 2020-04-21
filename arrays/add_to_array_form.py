'''
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

 

Example 1:

Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
Example 4:

Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
'''

def add_to_array_form(A, K):
    return [int(x) for x in str(int(''.join(str(x) for x in A)) + K)]

def add_to_array_form(A, K):
    carry, index = 0, len(A) - 1

    while K or carry:
        if index < 0: break
        A[index] += K % 10 + carry
        carry = A[index] // 10
        A[index] %= 10
        K //= 10
        index -= 1

    k_list = []
    while K or carry:
        digit = K % 10 + carry
        k_list.append(digit % 10)
        carry = digit // 10
        K //= 10

    return k_list[::-1] + A 


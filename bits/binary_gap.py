'''
Given a positive integer N, find and return the longest distance between two consecutive 1's in the binary 
representation of N.

If there aren't two consecutive 1's, return 0.

 

Example 1:

Input: 22
Output: 2
Explanation: 
22 in binary is 0b10110.
In the binary representation of 22, there are three ones, and two consecutive pairs of 1's.
The first consecutive pair of 1's have distance 2.
The second consecutive pair of 1's have distance 1.
The answer is the largest of these two distances, which is 2.
'''

def binary_gap(N):
    N, max_diff, prev = bin(N)[2:], 0, None
    
    for index, char in enumerate(N):
        if char == '1' and prev is None:
            prev = index
            continue
        if char == '1':
            max_diff = max(max_diff, index - prev)
            prev = index

    return max_diff 

def binary_gap_v2(N):
    N = bin(N)[2:]
    position_ones = []
    for index, char in enumerate(N):
        if char == '1': position_ones.append(index)
    max_diff = float('-inf')
    if len(position_ones) < 2: return 0
    for i in range(1, len(position_ones)):
        max_diff = max(max_diff, position_ones[i] - position_ones[i - 1])
    return max_diff
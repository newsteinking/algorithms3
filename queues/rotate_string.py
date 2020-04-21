'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A
 can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
'''

from collections import deque

def rotate_string(A, B):
    if A == B: return True
    if len(A) != len(B): return False
    que = deque([char for char in A])
    que2 = deque([char for char in B])
    
    for i in range(len(A)):
        que.append(que.popleft())
        if que == que2: return True
    
    return False 

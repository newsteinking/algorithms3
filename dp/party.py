'''
In Danceland, one person can party either alone or can pair up with another 
person. Can you find in how many ways they can party if there are N people in
 Danceland? Input Format
Given only argument A of type Integer, number of people in Danceland.
Output Format
Return a single integer N mod 10003, i.e number of ways people of Danceland can 
party.

Constraints
1 <= N <= 1e5 
Example
Input:
    N = 3

Output :
    4

Explanation :
    Let suppose three people are A, B, and C.
    There are only 4 ways to party as,
    (A, B, C) All party alone
    (AB, C) A and B party together and C party alone
    (AC, B) A and C party together and B party alone
    (BC, A) B and C party together and A party alone
    here 4 % 10003 = 4, so answer is 4.
'''

def party_v1(A):
    first, second = 1, 1
    
    for i in range(2, A + 1):
        third = second + (i - 1) * first 
        first = second
        second = third
        first %= 10003
        second %= 10003
    
    return second % 10003

def party_v2(A):
    memo = {}
    
    def dp(n):
        if n == 1:
            return 1 
        if n == 2:
            return 2
        if n in memo:
            return memo[n] 
        
        memo[n] = dp(n - 1) + (n - 1) * dp(n - 2)
        return memo[n] 
    
    return dp(A) % 10003
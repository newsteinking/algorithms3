'''
Max Sum Without Adjacent Elements
Given a 2 x N grid of integer, A, choose numbers such that the sum of the 
numbers is maximum and no two chosen numbers are adjacent horizontally, 
vertically or diagonally, and return it. Note: You can choose more than 2 
numbers. Input Format:
The first and the only argument of input contains a 2d matrix, A.
Output Format:
Return an integer, representing the maximum possible sum.
Constraints:
1 <= N <= 20000
1 <= A[i] <= 2000
Example:
Input 1:
    A = [   [1]
            [2]    ]

Output 1:
    2

Explanation 1:
    We will choose 2.

Input 2:
    A = [   [1, 2, 3, 4]
            [2, 3, 4, 5]    ]

Output 2:
    We will choose 3 and 5.
'''


def adjacent(nums_2d):
    memo = {}
    
    for i in range(len(nums_2d[0])):
        nums_2d[0][i] = max(nums_2d[0][i], nums_2d[1][i])
    nums_2d = nums_2d[0] 
    
    def dp(n):
        if n < 0: return 0 
        if n in memo: return memo[n] 
        
        memo[n] = max(nums_2d[n] + dp(n - 2), dp(n - 1))
        return memo[n] 
    
    return dp(len(nums_2d) - 1)
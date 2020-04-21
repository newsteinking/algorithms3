'''
Given an integer A, how many structurally unique BST's (binary search trees) 
exist that can store values 1...A? Input Format:
The first and the only argument of input contains the integer, A.
Output Format:
Return an integer, representing the answer asked in problem statement.
Constraints:
1 <= A <= 18
'''

def numTrees(A):
    memo = {}
    
    def count(n):
        if n == 0: return 1
        if n in memo: return memo[n]
        val = 0
        for i in range(1, n + 1):
            val += count(i - 1) * count(n - i)
            
        memo[n] = val
        return memo[n]
    
    return count(A)
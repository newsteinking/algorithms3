'''
Given an array of integers A representing chain of 2-D matices such that the 
dimensions of ith matrix is A[i-1] x A[i]. Find the most efficient way to 
multiply these matrices together. The problem is not actually to perform the 
multiplications, but merely to decide in which order to perform the multiplications. 
Return the minimum number of multiplications needed to multiply the chain. 
Input Format
The only argument given is the integer array A.
Output Format
Return the minimum number of multiplications needed to multiply the chain.
Constraints
1 <= length of the array <= 1000
1 <= A[i] <= 100
For Example
Input 1:
    A = [40, 20, 30, 10, 30]
Output 1:
    26000
    Explanation 1:
        Dimensions of A1 = 40 x 20
        Dimensions of A2 = 20 x 30
        Dimensions of A3 = 30 x 10
        Dimensions of A4 = 10 x 30
        First, multiply A2 and A3 ,cost = 20*30*10 = 6000
        Second, multilpy A1 and (Matrix obtained after multilying A2 and A3) =  
        40 * 20 * 10 = 8000
        Third, multiply (Matrix obtained after multiplying A1, A2 and A3) and A4 =  
        40 * 10 * 30 = 12000
        Total Cost = 12000 + 8000 + 6000 =26000

Input 2:
    A = [10, 20, 30] 
Output 2:
    6000
'''

def matrix_chain_multiplication(A):
    memo = {}
    
    def dp(i, j):
        if i == j: return 0
        if (i, j) in memo: return memo[(i, j)]
        
        minx = float('inf')
        for k in range(i, j):
            val = dp(i, k) + dp(k + 1, j) + A[i - 1] * A[k] * A[j]
            minx = min(minx, val)
        
        memo[(i,j )] = minx
        return memo[(i, j)]
    
    return dp(1, len(A) - 1)
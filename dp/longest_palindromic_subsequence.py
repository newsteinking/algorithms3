'''
Longest Pallindromic Subsequence
Given a strings A. Find the common pallindromic sequence ( A sequence which 
does not need to be contiguous and is a pallindrome), which is common in itself 
You need to return the length of such longest common subsequence. NOTE:
Your code will be run on multiple test cases (<=10). Try to come up with an 
optimised solution.
CONSTRAINTS
1 <= Length of A, B <= 10^3 + 5
EXAMPLE INPUT
A : "bebeeed"
EXAMPLE OUTPUT
4
EXPLANATION
The longest common pallindromic subsequence is "eeee", which has a length of 4
'''

def lps(word):
    memo = {}
    
    def dp(i, j):
        if i > j: return 0 
        if i == j: return 1 
        if word[i] == word[j] and i + 1 == j:
            return 2
        if (i, j) in memo:
            return memo[(i, j)]
        
        if word[i] == word[j]:
            memo[(i, j)] = 2 + dp(i + 1, j - 1)
        else:
            memo[(i, j)] = max(dp(i + 1, j), dp(i, j - 1))
        
        return memo[(i, j)]
    
    return dp(0, len(word) - 1)
        
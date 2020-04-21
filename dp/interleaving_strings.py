'''
Given A, B, C, find whether C is formed by the interleaving of A and B. 
Input Format:*
The first argument of input contains a string, A.
The second argument of input contains a string, B.
The third argument of input contains a string, C.
Output Format:
Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:
1 <= length(A), length(B), length(C) <= 150
Examples:
Input 1:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbcbcac"

Output 1:
    1

Explanation 1:
    "aa" (from A) + "dbbc" (from B) + "bc" (from A) + "a" (from B) + "c" (from A)

Input 2:
    A = "aabcc"
    B = "dbbca"
    C = "aadbbbaccc"

Output 2:
    0

Explanation 2:
    It is not possible to get C by interleaving A and B.
'''


def isInterleave(A, B, C):
    if len(A) + len(B) != len(C): return 0
    memo = {}
    
    def check(i, j):
        if i == -1 or j == -1:
            return True
        elif i == -1:
            return B[:j] == C[:j]
        elif j == -1:
            return A[:i] == C[:i]
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if C[i + j + 1] != A[i] and C[i + j + 1] != B[j]:
            memo[(i, j)] = False
        elif C[i + j + 1] == A[i] and C[i + j + 1] == B[j]:
            memo[(i, j)] = check(i, j - 1) or check(i - 1, j)
        elif C[i + j + 1] == A[i]:
            memo[(i, j)] = check(i - 1, j)
        else:
            memo[(i, j)] = check(i, j - 1)
        
        return memo[(i, j)]
    
    return int(check(len(A) - 1, len(B) - 1))
    
        
            
        
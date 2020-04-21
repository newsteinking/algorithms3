'''
Implement wildcard pattern matching with support for '?' and '*' for strings A and B.
'?' : Matches any single character.
'*' : Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial). Input Format:
The first argument of input contains a string A.
The second argument of input contains a string B.
Output Format:
Return 0 or 1:
    => 0 : If the patterns do not match.
    => 1 : If the patterns match.
Constraints:
1 <= length(A), length(B) <= 9e4
Examples :
Input 1:
    A = "aa"
    B = "a"

Output 1:
    0

Input 2:
    A = "aa"
    B = "aa"

Output 2:
    1

Input 3:
    A = "aaa"
    B = "aa"

Output 3:
    0

Input 4:
    A = "aa"
    B = "*"

Output 4:
    1

Input 5:
    A = "aa"
    B = "a*"

Output 5:
    1

Input 6:
    A = "ab"
    B = "?*"

Output 6:
    1

Input 7:
    A = "aab"
    B = "c*a*b"

Output 7:
    0
'''

def isMatch(s: str, p: str) -> bool:
    memo = {}
    prefix = 0
    while prefix < len(p) and p[prefix] == '*':
        prefix += 1
    
    def match(i, j):
        if i == -1 and j == -1: return True
        elif j == -1: return False
        elif i == -1: return True if j < prefix else False
        #elif i == -1: return True if p[:j + 1].count('*') == j + 1 else False
        elif (i, j) in memo: return memo[(i, j)]
        
        if p[j].isalpha():
            memo[(i, j)] = (s[i] == p[j]) and match(i - 1, j - 1)
        elif p[j] == '?':
            memo[(i, j)] = match(i - 1, j - 1)
        else:
            memo[(i, j)] = match(i, j - 1) or match(i - 1, j)
        
        return memo[(i, j)]
    
    return int(match(len(s) - 1, len(p) - 1))

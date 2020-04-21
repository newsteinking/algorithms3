'''
Given a string A, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively. Below is one possible representation of A = "great":
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children. For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great". Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great". 
 Given two strings A and B of the same length, determine if B is a scrambled string of S. 
 Input Format:
The first argument of input contains a string A.
The second argument of input contains a string B.
Output Format:
Return an integer, 0 or 1:
    => 0 : False
    => 1 : True
Constraints:
1 <= len(A), len(B) <= 50
Examples:
Input 1:
    A = "we"
    B = "we"

Output 1:
    1

Input 2:
    A = "phqtrnilf"
    B = "ilthnqrpf"

Output 2:
    0
'''

def isScramble(A, B):
    memo = {}
    
    def scramble(s1, s2):
        if (s1, s2) in memo:
            return memo[(s1, s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            memo[(s1, s2)] = False
            return False
        if s1 == s2:
            memo[(s1, s2)] = True
            return True
        
        for i in range(1, len(s1)):
            if (scramble(s1[:i], s2[:i]) and scramble(s1[i:], s2[i:]) or 
                scramble(s1[:i], s2[-i:]) and scramble(s1[i:], s2[:-i])):
                return True
        
        memo[(s1, s2)] = False
        return False
    
    return int(scramble(A, B))

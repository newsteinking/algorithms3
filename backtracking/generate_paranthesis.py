'''
Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

def generate_paran(n):
    result = []

    def backtrack(S='', left=0, right=0):
        if len(S) == 2*n:
            result.append(S)
            return
        if left < n:
            backtrack(S+'(', left+1, right)
        if right < left:
            backtrack(S+')', left, right+1)

    backtrack()
    return result


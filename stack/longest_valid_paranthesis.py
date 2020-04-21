'''
Given a string containing just the characters '(' and ')', find the length of the longest valid 
(well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

def longest_valid_paran(A):
    max_len = 0
    stack = [-1]

    for i in range(len(A)):
        if A[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)

    return max_len
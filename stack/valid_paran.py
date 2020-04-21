'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

def validate_parantheses(S:str) -> bool:
    stack = []
    map_brackets = {'{':'}', '[':']', '(':')'}
    for char in S:
        if char in map_brackets:
            stack.append(char)
        elif char in map_brackets.values():
            if stack == [] or char != map_brackets[stack.pop()]:
                return False
        else:
            return False 
    return stack == []
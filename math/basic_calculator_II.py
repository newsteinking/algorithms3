'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''

from collections import deque

def evaluate(exp):
    exp += ['+']
    stack, sign = list(), '+'
    for ch in exp:
        if type(ch) is int:
            num = ch
        else:
            if sign == '+': stack.append(num)
            if sign == '-': stack.append(-num)
            if sign == '*': stack.append(stack.pop()*num)
            if sign == '/': stack.append(int(stack.pop()/num))
            sign = ch

    return sum(stack) 

def build(exp):
    exp = exp.replace(' ', '')
    new_exp, num = list(['(']), 0 
    
    for ch in exp:
        if ch.isdigit():
            num = num*10 + int(ch)
        else:
            if num: new_exp.append(num)
            num = 0
            new_exp.append(ch)
    
    if num: new_exp.append(num)
    new_exp.append(')')
    
    return new_exp

def basic_calculator_two(exp):
    exp = build(exp)
    stack = []
    for val in exp:
        if val != ')':
            stack.append(val)
        else:
            partial_exp = deque()
            while stack[-1] != '(':
                partial_exp.appendleft(stack.pop())
            stack.pop()
            stack.append(evaluate(partial_exp))
    return sum(stack)


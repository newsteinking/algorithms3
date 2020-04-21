'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / 
operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
'''

def basic_calculator(exp):
    exp = exp.replace(' ', '') + '+0'
    stack, num, sign = [], 0, '+'

    for index,val in enumerate(exp):
        if val.isdigit():
            num = num*10 + int(val)
        else:
            if sign == '+': stack.append(num)
            if sign == '-': stack.append(-num)
            if sign == '*': stack.append(stack.pop()*num)
            if sign == '/': stack.append(int(stack.pop()/num))
            sign, num = val, 0
    
    return sum(stack)

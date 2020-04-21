'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

'''

def convert_to_title(n):
    result = ''
    while n >= 1:
        n -= 1
        result = chr(n%26 + ord('A')) + result
        n //= 26
        
    return result


'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
'''

def to_lower_case(str: str) -> str:
    result = ''
    for char in str:
        if 65 <= ord(char) <= 91:
            result += chr(ord(char) + 32)
        else:
            result += char
            
    return result



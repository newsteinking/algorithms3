'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement 
method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a 
single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
'''

def to_hex(num):
    if num == 0: return '0'
    mapping = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    if num < 0: num &= 0xffffffff
    result = []
    while num:
        digit = num & 15
        if 9 < digit < 16: digit = mapping[digit]
        else: digit = str(digit)
        result.append(digit)
        num >>= 4

    return ''.join(result[::-1])

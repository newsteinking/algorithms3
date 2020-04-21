'''Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string 
inside the square brackets is being repeated exactly k times. Note 
that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white 
spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any 
digits and that digits are only for those repeat numbers, k. For example, 
there won't be input like 3a or 2[4].
'''

from collections import deque
def decode_string(s):
    stack = []

    i = 0
    while i < len(s):
        while i < len(s) and s[i] != ']':
            stack.append(s[i])
            i += 1
        
        if i == len(s): break
        i += 1
        string = deque()
        while stack and stack[-1] != '[':
            string.insert(0, stack.pop())

        stack.pop()
        num = deque()
        while stack and stack[-1].isdigit():
            num.insert(0, stack.pop())
        num = int(''.join(num))

        result = num * ''.join(string)
        stack.append(result)

    return ''.join(stack)








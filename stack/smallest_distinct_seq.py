'''
Return the lexicographically smallest subsequence of text that contains all the distinct 
characters of text exactly once.

 

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"
 

Note:

1 <= text.length <= 1000
text consists of lowercase English letters.

'''

from collections import Counter

def smallest_subsequence(text):
    seen, count = set(), Counter(text)
    stack = []
    for val in text:
        count[val] -= 1
        if val in seen: continue
        while stack and stack[-1] > val and count[stack[-1]]:
            seen.remove(stack[-1])
            stack.pop()
        
        stack.append(val)
        seen.add(val)

    return ''.join(stack)


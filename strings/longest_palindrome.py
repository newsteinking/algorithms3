'''
Given a string which consists of lowercase or uppercase letters, find the length of the 
longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

from collections import Counter
def longest_palindrome(s):
    result = 0
    for v in Counter(s).values():
        result += v // 2 * 2
        if result % 2 == 0 and v % 2 == 1:
            result += 1
    
    return result 

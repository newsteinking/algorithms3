'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

def is_palindrome(x: int) -> bool:
    x = str(x)
    l, r = 0, len(x)-1
    while l < r:
        if x[l] != x[r]:
            return False
        l += 1
        r -= 1
    return True
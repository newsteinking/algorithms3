'''
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
'''



def shortest_palindrome_v2(s):

    def is_palindrome(word):
        return word == word[::-1]

    for i in range(len(A), -1, -1):
        if is_palindrome(A[:i]):
            return A[i:][::-1] + A

    return A
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

def partition_palindrome(s):
    result = []

    def backtrack(s = s, path = []):
        if not s:
            result.append(path[:])
            return 

        for i in range(1, len(s) + 1):
            if s[:i] == s[i - 1::-1]:
                path.append(s[:i])
                backtrack(s[i:], path)
                path.pop()

    backtrack()
    return result

def partition_palindrome_v2(s):
    result = []

    def is_palindrome(word1):
        return word1 == word1[::-1]

    def backtrack(s = s, path = []):
        if not s:
            result.append(path[:])
        else:
            for i in range(1, len(s) + 1):
                if is_palindrome(s[:i]):
                    path.append(s[:i])
                    backtrack(s[i:], path)
                    path.pop()

    backtrack()
    return result
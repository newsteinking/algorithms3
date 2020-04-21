'''
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters 
in A so that the result equals B.

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
'''

def buddy_strings(A, B):
    if len(A) != len(B): return False
    if A == B:
        seen = set()
        for a in A:
            if a in seen:
                return True 
            seen.add(a)
        return False

    first, second = None, None
    count = 0
    
    for i in range(len(A)):
        if A[i] != B[i]:
            if first == None: first = i
            elif second == None: second = i
            count += 1
    
    if count != 2: return False
    if A[first] == B[second] and B[first] == A[second]: return True 
    return False 
    
    
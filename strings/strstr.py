'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not 
part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


class RHash():
    
    def __init__(self,s):
        self.val = 0
        self.prime = 101
        self.base = 256
        self.shift = pow(self.base, len(s) - 1, self.prime)
        for c in s: 
            self.append(c)
    
    def append(self, c):
        self.val = (self.val * self.base + ord(c)) % self.prime

    def rmleft(self, c):
        self.val = (self.val - self.shift * ord(c) + self.prime) % self.prime 

    def __eq__(self, other):            
        return self.val == other.val
        
def strstr(haystack, needle):
    hl, nl = len(haystack), len(needle)
    if not needle: return 0
    if not haystack or nl > hl: return -1

    nh, hh = RHash(needle), RHash(haystack[:nl])
    if nh == hh and haystack[:nl] == needle:
        return 0

    for i in range(nl,hl ):
        hh.rmleft(haystack[i-nl])
        hh.append(haystack[i])
        if hh == nh and haystack[i-nl+1:i+1] == needle:
            return i - nl + 1
    return -1


def strstr_v2(haystack:str, needle:str) -> int:
    n = len(needle)
    if n == 0: return 0
    if n > len(haystack): return -1
    for i in range(len(haystack)-n+1):
        if haystack[i:i+n] == needle:
            return i
    return -1 

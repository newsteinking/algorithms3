'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or 
ore times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
'''

def gcd_of_strings(str1, str2):
    result = ''
    
    def gcd(a, b):
        length = len(b) / len(a)
        if int(length) != length:
            return False 
        return a * length == b

    result = ''
    for i in range(1, len(str1) + 1):
        sub_sequence = str1[:i]
        if len(sub_sequence) > len(str2): 
            return result
        if gcd(sub_sequence, a) and gcd(sub_sequence, b):
            result = sub_sequence

    return result 

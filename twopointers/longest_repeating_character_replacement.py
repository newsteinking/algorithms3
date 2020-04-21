'''
Given a string that consists of only uppercase English letters, you can replace any 
letter in the string with another letter at most k times. Find the length of a longest substring 
containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''

def character_replacement(s, k):
    count = {}
    start = max_count = result = 0
    for end in range(len(s)):
        count[s[end]] = count.get(s[end], 0) + 1
        max_count = max(max_count, count[s[end]])

        while end - start + 1 - max_count > k:
            count[s[start]] -= 1
            start += 1

        result = max(result, end - start + 1)

    return result 

def character_replacement_v2(s, k):
    longest = 0
    for i in range(ord('A'), ord('Z') + 1):
        start = cur_longest = 0
        count = 0
        for end in range(len(s)):
            if s[end] != chr(i): count += 1
            
            while count > k:
                if s[start] != chr(i): count -= 1
                start += 1
            
            longest = max(longest, end - start + 1)
                
    return longest

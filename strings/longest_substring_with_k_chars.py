'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) 
such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times
'''

from collections import Counter

def longest_repeating_substring(s, k):
    counter = Counter(s)
    for char in counter:
        if counter[char] < k:
            return max(longest_repeating_substring(t, k) for t in s.split(char))
    return len(s)    

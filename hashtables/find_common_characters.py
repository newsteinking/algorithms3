'''
Given an array A of strings made only from lowercase letters, return a list of all characters 
that show up in all strings within the list (including duplicates).  For example, if a character 
occurs 3 times in all strings but not 4 times, you need to include that character three times in 
the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
'''
from collections import Counter
import sys

def common_chars(A):
    common = set(A[0])
    result = list()

    for i in range(1, len(A)):
        common = common.intersection(set(A[i]))

    for char in common:
        result += min([word.count(char) for word in A]) * char

    return sorted(result)

def common_chars_v2(A):
    counter_list = [Counter(x) for x in A]
    result = []
    for i in range(ord('a'), ord('z') + 1):
        common = sys.maxsize
        for count in counter_list:
            if chr(i) in count:
                common = min(common, count[chr(i)])
            else:
                break
        else:
            result += [chr(i)] * common 
    
    return result 


    
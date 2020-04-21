'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a 
substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a 
substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''

def repeated_string_match(A: str, B: str) -> int:
    count = (len(B) - 1) // len(A) + 1
    A1 = A * count
    A2 = A * (count + 1)
    
    if B in A1: return count
    if B in A2: return count + 1
    return -1


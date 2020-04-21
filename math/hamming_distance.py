'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

def hamming_distance(x, y):
    x = bin(x)
    y = bin(y)
    count = 0
    
    x = x[2:]
    y = y[2:]
    
    if len(x) > len(y):
        x, y = y, x
    
    x = '0' * (len(y) - len(x)) + x
    
    for i in range(len(x)):
        if x[i] != y[i]: count += 1
    
    return count 


def hamming_distance_v2(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count('1')

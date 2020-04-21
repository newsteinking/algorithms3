'''
You have a total of n coins that you want to form in a staircase shape, where every k-th 
row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''

def arranging_coins(n):
    left, right = 0, n 
    result = 0
    while left <= right:
        mid = (left + right) // 2
        total = (mid * (mid + 1)) // 2

        if n >= total:
            left = mid + 1
            result = mid 
        else:
            right = mid - 1

    return result
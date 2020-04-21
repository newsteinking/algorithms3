'''
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the 
number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
'''
from collections import Counter

def num_tile_possible(tiles):
    count = Counter(tiles)
    fact_divisor = 1
    for val in count.values():
        fact_divisor *= math.factorial(val)

    result = 0
    for i in range(1, len(tiles)):
        number = math.factorial(len(tiles)) // math.factorial(len(tiles) - i)
        number //= fact_divisor
        result += number 

    return result

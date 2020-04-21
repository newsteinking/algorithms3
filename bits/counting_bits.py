'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate 
the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do 
it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in 
c++ or in any other language.
'''

def count_bits(num):
    num_of_bits = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

    def count_set_bits(num):
        if num == 0: return num_of_bits[0]
        nibble = 0
        nibble = num & 15
        return num_of_bits[nibble] + count_set_bits(num >> 4)

    return [count_set_bits(x) for x in range(num + 1)]


def count_bits_v2(num):
    counts = [0] * (num + 1)
    for i in range(num + 1):
        count, val = 0, i
        while val:
            val &= (val - 1)
            count += 1
        counts[i] = count 

    return counts

def count_bits_v3(num):
    return [bin(x)[2:].count('1') for x in range(num + 1)]


def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return sorted([str(x) for x in range(1, n + 1)])


'''
The Hamming distance between two integers is the number of positions at which the corresponding 
bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
Note:
Elements of the given array are in the range of 0 to 10^9
Length of the array will not exceed 10^4.
'''

def total_hamming_distance(nums):
    total = 0
    for i in range(32):
        set_bits = 0
        for num in nums:
            if num & (1 << i): set_bits += 1
        total += set_bits * (len(nums) - set_bits)
    return total

def total_hamming_distance_v2(nums):
    result = 0
    count = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            val1, val2 = nums[i], nums[j]
            for _ in range(32):
                count += 1
                result += (val1 & 1 != val2 & 1)
                val1 >>= 1
                val2 >>= 1
    return count 



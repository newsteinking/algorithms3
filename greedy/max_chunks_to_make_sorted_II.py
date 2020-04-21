'''
Given an array arr of integers (not necessarily distinct), we split the array into some number of 
"chunks" (partitions), and individually sort each chunk.  After concatenating them, the result 
equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
'''
from collections import Counter

def max_chunks_to_make_sorted(arr):
    sorted_count = Counter()
    original_count = Counter()

    sorted_arr = sorted(arr)
    chunks = 0

    for index, val in enumerate(arr):
        sorted_count[sorted_arr[index]] += 1
        original_count[val] += 1
        if sorted_count == original_count:
            chunks += 1

    return chunks 




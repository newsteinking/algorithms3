'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is 
the array's size.
'''
import heapq
def k_most_frequent(nums, k):
    nums_map = {}
    for num in nums:
        nums_map[num] = nums_map.get(num, 0) + 1

    #heap = [(-value, key) for key, value in nums_map.items()]
    #largest = [x[1] for x in heapq.nsmallest(k, nums_map.keys())]
    return [x[1] for x in heapq.nlargest(k, ((value, key) for key, value in nums_map.items()))]


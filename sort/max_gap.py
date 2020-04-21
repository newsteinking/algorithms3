'''
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed 
integer range.
Try to solve it in linear time/space.
'''

class Bucket:

    def __init__(self):
        self.used = False 
        self.min_val = float('inf')
        self.max_val = float('-inf')

def max_gap(nums):
    if len(nums) < 2 : return 0 
    
    min_nums = min(nums)
    max_nums = max(nums)

    bucket_size = max(1, (max_nums - min_nums) // (len(nums) - 1))
    bucket_num = (max_nums - min_nums) // bucket_size + 1

    buckets = [Bucket() for _ in range(bucket_num)] 

    for val in nums:
        index = (val - min_nums) // bucket_size
        buckets[index].used = True 
        buckets[index].min_val = min(buckets[index].min_val, val)
        buckets[index].max_val = max(buckets[index].max_val, val)

    gap, prev = 0, None
    for bucket in buckets:
        if not bucket.used:
            continue
        if prev: gap = max(gap, bucket.min_val - prev)
        prev = bucket.max_val

    return gap


def max_gap_v2(nums):
    gap = 0
    nums.sort()
    for i in range(1, len(nums)):
        gap = max(gap, nums[i] - nums[i - 1])
    return gap
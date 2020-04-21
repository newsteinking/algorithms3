'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no 
middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
'''
import bisect 
from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


class MedianFinder2:

    def __init__(self):
        self.nums = []

    def add_num(self, x):
        if not self.nums:
            self.nums.append(float(x))
        else:
            self.nums.insert(bisect.bisect_left(self.nums, x), float(x))

    def find_median(self):
        mid = len(self.nums) // 2
        if len(self.nums) % 2:
            return self.nums[mid]
        else:
            return (self.nums[mid] + self.nums[mid - 1]) / 2 

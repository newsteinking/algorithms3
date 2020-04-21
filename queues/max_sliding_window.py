'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''

from collections import deque
class MaxQue:
    def __init__(self):
        self.que = deque()

    def push(self, x):
        count = 0
        while self.que and self.que[-1][0] < x:
            count += self.que[-1][1] + 1
            self.que.pop()
        self.que.append([x, count])
    
    def pop(self):
        if self.que[0][1] > 0:
            self.que[0][1] -= 1
            return
        self.que.popleft()
    
    def get_max(self):
        return self.que[0][0]



from heapq import *
import itertools

class PQMax:
    
    def __init__(self):
        self.pq = []                       
        self.entry_finder = {}              
        self.REMOVED = '<removed-task>'           
        self.counter = itertools.count()

    def add_task(self, task, priority):
        if task in self.entry_finder:
            self.remove_task(task, priority)
        entry = [task, next(self.counter), priority]
        self.entry_finder[(task, priority)] = entry
        heappush(self.pq, entry)

    def remove_task(self, task, priority):
        entry = self.entry_finder.pop((task, priority))
        entry[-1] = self.REMOVED

    def pop_task(self):
        while self.pq:
            task, _, priority = heappop(self.pq)
            if priority is not self.REMOVED:
                del self.entry_finder[(task, priority)]
                return task, priority
        raise KeyError('pop from an empty priority queue')

    def get_max(self):
        maxx, index = self.pop_task()
        self.add_task(maxx, index)
        return -maxx

    
def max_sliding_window(nums, k):
    pq = PQMax()
    
    for i in range(k):
        pq.add_task(-nums[i], i)
    
    result = []
    result.append(pq.get_max())

    for i in range(k, len(nums)):
        pq.remove_task(-nums[i - k], i - k)
        pq.add_task(-nums[i], i)
        result.append(pq.get_max())
    
    return result 



def max_sliding_window_v2(nums, k: int):
    que = MaxQue()
    result = []
    for i in range(k):
        que.push(nums[i])
    
    result.append(que.get_max())
    
    for i in range(k, len(nums)):
        que.pop()
        que.push(nums[i])
        result.append(que.get_max())
    
    return result

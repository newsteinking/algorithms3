'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. 
Any permutation of 
[1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''

import random
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)
        
    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            index = random.randrange(i, len(self.array))
            self.array[index], self.array[i] = self.array[i], self.array[index]
        return self.array


class Solution2:

    def __init__(self, nums: 'List[int]'):
        self.nums = nums

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.nums, key=lambda x: random.random())

class Solution3:

    def __init__(self, nums: 'List[int]'):
        self.nums = nums

    def reset(self) -> 'List[int]':
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> 'List[int]':
        """
        Returns a random shuffling of the array.
        """
        return sorted(self.nums, key=lambda x: random.random())

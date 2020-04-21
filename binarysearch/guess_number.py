'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example :

Input: n = 10, pick = 6
Output: 6
'''

class GuessGame:
    def __init__(self, pick, pick_range):
        self.pick = pick
        self.pick_range = pick_range

    def guess(self, n):
        if self.pick < n: return -1
        if self.pick > n: return 1
        if self.pick == n: return 0


    def guess_number(self):
        left, right = 0, self.pick_range
        while left <= right:
            mid = (left + right) // 2
            if self.guess(mid) == 0:
                return mid
            elif self.guess(mid) == 1:
                left = mid + 1
            else:
                right = mid - 1

        return -1 


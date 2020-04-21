'''
Given a list of non negative integers, arrange them such that they form the
 largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
'''

class Compare(str):
    def __lt__(x, y):
        return x+y > y+x
    
def largest_number(nums) -> str:
    nums = ''.join(sorted(map(str, nums), key=Compare))
    return '0' if nums[0] == '0' else nums


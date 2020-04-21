'''
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", 
"Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
'''

def relative_ranks(nums):
    scores = sorted([(score, num) for num, score in enumerate(nums)], reverse = True)
    ranks = [None] * len(nums)
    
    for index, val in enumerate(scores): 
        ranks[val[1]] = str(index + 1)
        
    if len(ranks) > 0: ranks[scores[0][1]] = 'Gold Medal'
    if len(ranks) > 1: ranks[scores[1][1]] = 'Silver Medal'
    if len(ranks) > 2: ranks[scores[2][1]] = 'Bronze Medal'
    
    return ranks




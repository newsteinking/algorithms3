'''
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
'''
def friends_of_ages(ages) -> int:
    count = [0] * 121

    for age in ages:
        count[age] += 1

    requests = 0
    for age_A, count_A in enumerate(count):
        for age_B, count_B in enumerate(count):
            if age_B <= 0.5 * age_A + 7: continue
            if age_B > age_A: continue
            if age_B > 100 and age_A < 100: continue
            requests += count_A * count_B
            if age_A == age_B: requests -= count_A

    return requests
# def friend_requests(ages) -> int:
#     count = [0] * 121
#
#     for age in ages:
#         count[age] += 1
#
#     requests = 0
#     for age_A, count_A in enumerate(count):
#         for age_B, count_B in enumerate(count):
#             if age_B <= 0.5 * age_A + 7: continue
#             if age_B > age_A: continue
#             if age_B > 100 and age_A < 100: continue
#             requests += count_A * count_B
#             if age_A == age_B: requests -= count_A
#
#     return requests


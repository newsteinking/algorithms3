'''
Finding Position
Given an integer A which denotes the number of people standing in the queue. A selection process 
follows a rule where people standing on even positions are selected. Of the selected people a queue 
is formed and again out of these only people on even position are selected.  This continues until we 
are left with one person. Find and return the position of that person in the original queue. 
Input Format
The only argument given is integer A.
Output Format
Return the position of the last selected person in the original queue.
Constraints
1 <= A <= 10^9
For Example
Input 1:
    A = 10
Output 1:
    8

Input 2:
    A = 20
Output 2:
    16
'''

def finding_position(A):
    powers_of_two = [1]
    n = 1
    while True:
        power = 2 ** n
        powers_of_two.append(power)
        if A < power:
            break
        n += 1
    if A in powers_of_two:
        return A 

    i = 0
    while i < len(powers_of_two):
        if powers_of_two[i] > A:
            break
        i += 1    
    return powers_of_two[i - 1]

def finding_position_v2(A):
    nums = [x for x in range(1, A + 1)]

    while len(nums) > 1:
        for i in range(0, len(nums), 2):
            nums[i] = None
        nums = [x for x in nums if x]

    return nums[0]
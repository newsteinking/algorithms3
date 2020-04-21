'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
'''

def valid_time(A):
    largest = -1
    A.sort()

    def valid(time):
        nonlocal largest
        a, b, c, d = time 
        hours, minutes = 10 * a + b, 10 * c + d 
        time = 60 * hours + minutes
        if hours < 24 and minutes < 60 and time > largest:
            largest = time

        
    def backtrack(temp = [], used = set()):
        nonlocal largest
        if len(temp) == 4:
            valid(temp)
        else:
            for i in range(4):
                if i in used or i > 0 and A[i] == A[i - 1] and i - 1 not in used:
                    continue
                used.add(i)
                temp.append(A[i])
                backtrack(temp)
                temp.pop()
                used.remove(i)

    backtrack()
    return '{:02}:{:02}'.format(*divmod(largest, 60)) if largest > -1 else '' 

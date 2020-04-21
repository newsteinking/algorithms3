'''
Given a list of 24-hour clock time points in "Hour:Minutes" format, 
find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't 
exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''

def min_time(timepoints):
    for index, time in enumerate(timepoints):
        hours, minutes = time.split(':')
        if hours == '00': hours = 24
        timepoints[index] = int(hours)*60 + int(minutes) 
        
    timepoints.sort()
    minx = float('inf')

    for i in range(len(timepoints)-1):
        if timepoints[i+1] - timepoints[i] < minx:
            minx = timepoints[i+1] - timepoints[i]
   
    return minx        



'''
You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information 
about the i-th trip: the number of passengers that must be picked up, and the locations to pick them 
up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's 
initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
'''

def car_pooling(trips, capacity):
    start_que = []
    end_que = []

    for i in range(len(trips)):
        start_que.append((trips[i][1], trips[i][0]))
        end_que.append((trips[i][2], trips[i][0]))
    
    start_que.sort(reverse = True)
    end_que.sort(reverse = True)
    
    current_capacity = 0
    while start_que:
        current_start, people = start_que.pop()
        while current_start >= end_que[-1][0]:
            current_end, end_people = end_que.pop()
            current_capacity -= end_people
        if current_capacity + people > capacity: return False
        current_capacity += people

    return True
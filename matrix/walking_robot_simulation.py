'''

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of 
three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. 

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead 
(but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)
'''

def walking_robot_simulation(commands, obstacles):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = di = 0
    obstacleSet = set(map(tuple, obstacles))
    ans = 0

    for cmd in commands:
        if cmd == -2:  #left
            di = (di - 1) % 4
        elif cmd == -1:  #right
            di = (di + 1) % 4
        else:
            for k in range(cmd):
                if (x+dx[di], y+dy[di]) not in obstacleSet:
                    x += dx[di]
                    y += dy[di]
                    ans = max(ans, x*x + y*y)

    return ans    

def walking_robot_simulation_v2(commands, obstacles):
    directions = {('north', -2):'west', ('north', -1):'east',
                  ('east', -2):'north', ('east', -1):'south',
                  ('west', -2):'south', ('west', -1):'north',
                  ('south', -2):'east', ('south', -1):'west'}
    
    direction = 'north'
    position = (0, 0)
    obstacles = set(tuple(x) for x in obstacles)

    for command in commands:
        if command == -1: 
            direction = directions[(direction, -1)]
        elif command == -2: 
            directions = directions[(direction, -2)]
        else:
            for i in range(command):
                if direction == 'north':
                    new_position = (position[0], position[1] + 1)
                    if new_position in obstacles: break
                    position = new_position    
                
                if direction == 'south':
                    new_position = (position[0], position[1] - 1)
                    if new_position in obstacles: break
                    position = new_position    
                
                if direction == 'east':
                    new_position = (position[0] + 1, position[1])
                    if new_position in obstacles: break
                    position = new_position    
                
                if direction == 'west':
                    new_position = (position[0] - 1, position[1])
                    if new_position in obstacles: break
                    position = new_position

    return position     




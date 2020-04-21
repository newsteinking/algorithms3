'''
Three stones are on a number line at positions a, b, and c.

Each turn, let's say the stones are currently at positions x, y, z with x < y < z.  You pick up the

 stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return 
the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

 

Example 1:

Input: a = 1, b = 2, c = 5
Output: [1, 2]
Explanation: Move stone from 5 to 4 then to 3, or we can move it directly to 3.
Example 2:

Input: a = 4, b = 3, c = 2
Output: [0, 0]
Explanation: We cannot make any moves.
 

Note:

1 <= a <= 100
1 <= b <= 100
1 <= c <= 100
a != b, b != c, c != a
'''

def moving_stones(a, b, c):
    a, b, c = sorted([a, b, c])
    minx = 0
    maxx = c - a - 2
    if a + 1 == b or b + 1 == c: minx = 1
    elif a + 2 == b or b + 2 == c: minx = 1
    else: minx = 2
    if maxx == 0: minx = 0
    return [minx, maxx]
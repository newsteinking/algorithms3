'''

There are A coins (Assume A is even) in a line. Two players take turns to 
take a coin from one of the ends of the line until there are no more coins left. 
The player with the larger amount of money wins. Assume that you go first.
 Return the maximum amount of money you can win. Input Format:
The first and the only argument of input contains an integer array, A.
Output Format:
Return an integer representing the maximum amount of money you can win.
Constraints:
1 <= length(A) <= 500
1 <= A[i] <= 1e5
Examples:
Input 1:
    A = [1, 2, 3, 4]

Output 1:
    6

Explanation 1:

    You      : Pick 4
    Opponent : Pick 3
    You      : Pick 2
    Opponent : Pick 1

    Total money with you : 4 + 2 = 6

Input 2:
    A = [5, 4, 8, 10]

Output 2:
    15

Explanation 2:

    You      : Pick 10
    Opponent : Pick 8
    You      : Pick 5
    Opponent : Pick 4

    Total money with you : 10 + 5 = 15
'''

# def maxcoin(self, A):
#     memo = {}
#
#     def coins(start, end, sumx):
#         if start + 1 == end:
#             return max(A[start], A[end])
#         if (start, end) in memo:
#             return memo[(start, end)]
#         memo[(start, end)] = max(sumx - coins(start, end - 1, sumx - A[end]),
#                                  sumx - coins(start + 1, end, sumx - A[start]))
#         return memo[(start, end)]
#
#     return coins(0, len(A) - 1, sum(A))

def coins_in_a_line(A):
    memo = {}

    def coins(start, end, sumx):
        if start + 1 == end:
            return max(A[start], A[end])
        if (start, end) in memo:
            return memo[(start, end)]
        memo[(start, end)] = max(sumx - coins(start, end - 1, sumx - A[end]),
                                 sumx - coins(start + 1, end, sumx - A[start]))
        return memo[(start, end)]

    return coins(0, len(A) - 1, sum(A))
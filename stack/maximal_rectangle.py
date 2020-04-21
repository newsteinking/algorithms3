'''

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing 
only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

    
def next_smaller(smaller, A):
    ns, stack = [-1] * len(A), []
    if smaller: x = range(len(A))
    else: x = range(len(A) -1, - 1, -1)

    for i in x:
        while stack and A[stack[-1]] > A[i]:
            ns[stack[-1]] = i
            stack.pop()
        stack.append(i)

    return ns

def largest_histogram(self, A):
    ns = next_smaller(True, A)
    ps = next_smaller(False, A)
    max_area = 0
    for i in range(len(A)):
        left = 0 if ps[i] == -1 else ps[i] + 1
        right = len(A) - 1 if ns[i] == -1 else ns[i] - 1
        max_area = max(max_area, A[i] * (right - left + 1))

    return max_area

def maximalRectangle(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(A[i][j])
            if i == 0 or A[i][j] == 0: continue
            A[i][j] += A[i - 1][j]
    
    max_area = 0
    for row in A:
        area = largest_histogram(row)
        max_area = max(max_area, area)
    
    return max_area
    

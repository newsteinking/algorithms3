'''
Given n non-negative integers representing the histogram's bar height where the 
width of each bar is 1, find the area of largest rectangle in the histogram.

Input: [2,1,5,6,2,3]
Output: 10
'''

def largest_rectangle_area(heights):

    def next_smaller(smaller):
        ns, stack = [-1] * len(A), []
        if smaller: x = range(len(A))
        else: x = range(len(A) -1, - 1, -1)
        
        for i in x:
            while stack and A[stack[-1]] > A[i]:
                ns[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        return ns
        
    ns = next_smaller(True)
    ps = next_smaller(False)
    max_area = 0
    for i in range(len(A)):
        left = 0 if ps[i] == -1 else ps[i] + 1
        right = len(A) - 1 if ns[i] == -1 else ns[i] - 1
        max_area = max(max_area, A[i] * (right - left + 1))
    
    return max_area
        

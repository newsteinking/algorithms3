'''
Given a matrix of integers A of size N x 3 representing the dimensions of N 
rectangular 3-D boxes, where A[i][0] represents the height of the ith box, A[i][1] 
represents the widht of the ith box and A[i][2] represents the length of the ith box. 
ou want to create a stack of boxes which is as tall as possible, but you 
can only stack a box on top of another box if the dimensions of the 2-D base 
of the lower box are each strictly larger than those of the 2-D base of the h
igher box. You can rotate a box so that any side functions as its base. It is
 also allowable to use multiple instances of the same type of box. Find and 
 return the maximum height of stack achievable. 
Input Format
The only argument given is the integer matrix A.
Output Format
Return the maximum height of stack achievable.
Constraints
1 <= N <= 1000
1 <= A[i][0], A[i][1], A[i][2] <= 10^6
For Example
Input 1:
    A = [   [4, 6, 7]
            [1, 2, 3]
            [4, 5, 6]
            [1, 2, 3]   ]
Output 1:
    60
    Explanation 1:
        Following are all rotations of the boxes in decreasing order of base area:
        10 x 12 x 32
        12 x 10 x 32
        32 x 10 x 12
        4 x 6 x 7
        4 x 5 x 6
        6 x 4 x 7
        5 x 4 x 6
        7 x 4 x 6
        6 x 4 x 5
        1 x 2 x 3
        2 x 1 x 3
        3 x 1 x 2

        The height 60 is obtained by boxes
        [ [3, 1, 2], [1, 2, 3], [6, 4, 5], [4, 5, 6], [4, 6, 7], [32, 10, 12], [10, 12, 32] ]


Input 2:
    A = [   [4, 5, 6]
            [10, 12, 14]    ]

Output 2:
    34
'''

class Box: 
      
    # Representation of a box 
    def __init__(self, h, w, d): 
        self.h = h 
        self.w = w 
        self.d = d 
  
    def __lt__(self, other): 
        return self.d * self.w < other.d * other.w 
  
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, arr):
        n = len(arr)
        arr = [Box(arr[i][0], arr[i][1], arr[i][2]) for i in range(len(arr))]
        rot = [Box(0, 0, 0) for _ in range(3 * n)] 
        index = 0
      
        for i in range(n): 
      
            # Copy the original box 
            rot[index].h = arr[i].h 
            rot[index].d = max(arr[i].d, arr[i].w) 
            rot[index].w = min(arr[i].d, arr[i].w) 
            index += 1
      
            # First rotation of the box 
            rot[index].h = arr[i].w 
            rot[index].d = max(arr[i].h, arr[i].d) 
            rot[index].w = min(arr[i].h, arr[i].d) 
            index += 1
      
            # Second rotation of the box 
            rot[index].h = arr[i].d 
            rot[index].d = max(arr[i].h, arr[i].w) 
            rot[index].w = min(arr[i].h, arr[i].w) 
            index += 1
      
        # Now the number of boxes is 3n 
        n *= 3
      
        # Sort the array 'rot[]' in non-increasing  
        # order of base area 
        rot.sort(reverse = True) 
      
        # Uncomment following two lines to print  
        # all rotations  
        # for i in range(n): 
        #    print(rot[i].h, 'x', rot[i].w, 'x', rot[i].d) 
      
        # Initialize msh values for all indexes 
        # msh[i] --> Maximum possible Stack Height  
        # with box i on top 
        msh = [0] * n 
      
        for i in range(n): 
            msh[i] = rot[i].h 
      
        # Compute optimized msh values 
        # in bottom up manner 
        for i in range(1, n): 
            for j in range(0, i): 
                if (rot[i].w < rot[j].w and 
                    rot[i].d < rot[j].d): 
                    if msh[i] < msh[j] + rot[i].h: 
                        msh[i] = msh[j] + rot[i].h 
      
        return max(msh)
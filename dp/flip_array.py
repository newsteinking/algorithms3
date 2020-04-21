'''
Given an array of positive elements, you have to flip the sign of some of 
its elements such that the resultant sum of the elements of array should be 
minimum non-negative(as close to zero as possible). Return the minimum no. of 
elements whose sign needs to be flipped such that the resultant sum is minimum 
non-negative. Constraints:
 1 <= n <= 100
Sum of all the elements will not exceed 10,000. Example:
A = [15, 10, 6]
ans = 1 (Here, we will flip the sign of 15 and the resultant sum will be 1 )
A = [14, 10, 4]
ans = 1 (Here, we will flip the sign of 14 and the resultant sum will be 0)
'''

def flip_array(A):
    n = len(A)

    def helper(i, cur, memo={}):
        if i == n or cur == 0:
            return (cur, 0)
        if (i, cur) in memo:
            return memo[(i, cur)]
        res, flip = helper(i+1, cur)  
        if 2*A[i] <= cur:             
            res2, flip2 = helper(i+1, cur-2*A[i])
            res, flip = min((res, flip), (res2, flip2+1))
        memo[(i, cur)] = (res, flip)
        return res, flip
   
    return helper(0, sum(A))[1]
        
    
    
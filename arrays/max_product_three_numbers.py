'''
Given an integer array, find three numbers whose product is maximum and 
output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
'''

def max_product_three_numbers(nums) -> int:
    min1 = min2 = float('inf')
    max1 = max2 = max3 = float('-inf')
    
    for number in nums:
        if number <= min1:
            min2 = min1
            min1 = number
        elif number <= min2:
            min2 = number 


        if number >= max1:
            max3 = max2
            max2 = max1
            max1 = number
        elif number >= max2:
            max3 = max2
            max2 = number
        else: 
            max3 = number 
 
    return max(min1*min2*max1, max1*max2*max3)
        


        
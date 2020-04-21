'''
An image is represented by a 2-D array of integers, each integer representing the pixel value 
of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill,
 and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally 
to the starting pixel of the same color as the starting pixel, plus any pixels 
connected 4-directionally to those pixels (also with the same color as the starting pixel), and so 
on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
'''

def flood_fill(image, sr, sc, new_color):

    def dfs(i, j):
        if not 0 <= i < len(image) or not 0 <= j < len(image[0]):
            return

        if image[i][j] != start_color:
            return

        image[i][j] = new_color

        directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for direction in directions:
            dfs(direction[0], direction[1])

    start_color = image[sr][sc]
    dfs(sr, sc)
    return image
'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first 
take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to 
finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

'''

from collections import defaultdict

def course_order(num_courses, prerequisites) -> bool:
    graph = defaultdict(list)
    for course in prerequisites:
        graph[course[0]].append(course[1])

    visited = [0 for x in range(num_courses)]

    def dfs(vertex):
        if visited[vertex] == -1:
            return False 
        if visited[vertex] == 1:
            return True 

        visited[vertex] = -1
        for node in graph[vertex]:
            if not dfs(node):
                return False
        visited[vertex] = 1
        return True

    for i in range(num_courses):
        if not dfs(i):
            return False 
    return True























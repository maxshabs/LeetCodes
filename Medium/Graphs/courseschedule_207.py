# Solution for LeetCode Problem 207: Course Schedule
# Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
#                  Each course and each prerequisite pair is visited once during the traversal.
# Space Complexity: O(V + E), for the adjacency list representation of the graph and the recursion stack.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list (prerequisite map)
        pre_map = {i: [] for i in range(numCourses)}
        for pre, course in prerequisites:
            pre_map[course].append(pre)
        
        visited = set()

        # Depth First Search to detect cycles
        def dfs(course: int) -> bool:
            # Cycle detected
            if course in visited:
                return False
            
            # No prerequisites, course can be completed
            if pre_map[course] == []:
                return True
            
            visited.add(course)

            # Visit all prerequisites
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False
            
            # Mark course as completed
            visited.remove(course)
            pre_map[course] = []  # Clear prerequisites to avoid re-checking
            return True
        
        # Check each course for cycles
        for crs in pre_map:
            if not dfs(crs):
                return False
        
        return True

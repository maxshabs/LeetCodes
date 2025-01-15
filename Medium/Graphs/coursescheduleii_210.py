# Solution for LeetCode Problem 210: Course Schedule II
# Time Complexity: O(n + m), where n is the number of courses (nodes) and m is the number of prerequisites (edges). 
#                  Each course is visited once, and the prerequisites are iterated over once.
# Space Complexity: O(n + m), for the adjacency list representation of the graph and the recursion stack in the DFS.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {i: [] for i in range(numCourses)}  # Create adjacency list for courses
        for course, pre in prerequisites:
            pre_map[course].append(pre)
        
        result = []  # Stores the topological order
        visited, visiting = set(), set()  # Track visited and visiting nodes
        
        def dfs(course: int) -> bool:
            if course in visiting:  # Cycle detected
                return False
            
            if course in visited:  # Already processed
                return True
            
            visiting.add(course)  # Mark as visiting
            
            for pre in pre_map[course]:  # Visit all prerequisites
                if not dfs(pre):
                    return False
            
            visiting.remove(course)  # Mark as visited
            visited.add(course)
            result.append(course)  # Add course to result
            
            return True
        
        for course in pre_map:  # Iterate over all courses
            if not dfs(course):
                return []  # Cycle detected, return empty list
        
        return result  # Return topological order

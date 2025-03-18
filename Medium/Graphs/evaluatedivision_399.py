# Solution for LeetCode Problem 399: Evaluate Division
# Time Complexity: O(Q * (V + E)), where:
#   - V is the number of unique variables (nodes in the graph).
#   - E is the number of given equations (edges in the graph).
#   - Q is the number of queries.
#   - Building the graph takes O(V + E).
#   - Each query runs a DFS, taking O(V + E) in the worst case.
#   - Total complexity: O(Q * (V + E)).
# Space Complexity: O(V + E), as we store the graph.

from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Evaluates division queries using given equations and their numerical values.

        Parameters:
        equations (List[List[str]]): List of equations in the form [["A", "B"], ["C", "D"], ...].
        values (List[float]): Corresponding values for equations, e.g., A / B = value.
        queries (List[List[str]]): Queries to evaluate, e.g., ["A", "C"].

        Returns:
        List[float]: The results for each query, or -1.0 if no valid path exists.
        """
        # Step 1: Construct the graph using a nested defaultdict
        graph_dict = defaultdict(dict)

        # Populate the graph with direct relations
        for i in range(len(equations)):
            dividend, divisor = equations[i][0], equations[i][1]
            graph_dict[dividend][divisor] = values[i]  # A / B = values[i]
            graph_dict[divisor][dividend] = 1 / values[i]  # B / A = 1 / values[i]

        def dfs(src: str, dst: str, length: float, visited: set) -> float:
            """
            Performs DFS to find a valid division path between src and dst.

            Parameters:
            src (str): The starting variable.
            dst (str): The target variable.
            length (float): The current accumulated division result.
            visited (set): Set of visited variables to prevent cycles.

            Returns:
            float: Computed division result or -1 if no valid path exists.
            """
            # If either variable is not in the graph, return -1
            if src not in graph_dict or dst not in graph_dict or src in visited:
                return -1.0
            
            # If src and dst are the same, return accumulated length
            if src == dst:
                return length
            
            visited.add(src)  # Mark node as visited
            
            # Explore neighbors recursively
            for neighbor, weight in graph_dict[src].items():
                result = dfs(neighbor, dst, length * weight, visited)
                if result != -1:
                    return result  # If a valid path is found, return result
            
            return -1.0  # If no valid path found

        # Step 2: Process each query using DFS
        res_list = []
        for src, dst in queries:
            visited = set()  # Reset visited set for each query
            res_list.append(dfs(src, dst, 1.0, visited))

        return res_list  # Return the list of results

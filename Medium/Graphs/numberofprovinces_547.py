# Solution for LeetCode Problem 547: Number of Provinces
# Time Complexity: O(N^2), where N is the number of cities.
#   - We visit each city once and check all its connections (adjacency matrix traversal).
# Space Complexity: O(N), as we store the visited status of each city in a list.

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Finds the number of provinces (connected components) in an undirected graph.

        Parameters:
        isConnected (List[List[int]]): An adjacency matrix representing connections between cities.
        
        Returns:
        int: The number of connected provinces.
        """
        n = len(isConnected)  # Number of cities (nodes in the graph)
        visited = [0] * n  # List to track visited cities

        def dfs(city: int) -> None:
            """
            Performs depth-first search (DFS) to mark all cities connected to the given city.

            Parameters:
            city (int): The current city being visited.
            """
            visited[city] = 1  # Mark the city as visited
            
            # Explore all possible connections to other cities
            for c, is_con in enumerate(isConnected[city]):
                if visited[c] == 0 and is_con == 1:  # If connected and not visited
                    dfs(c)

        num_prov = 0  # Counter for the number of provinces (connected components)

        # Traverse all cities
        for i in range(n):
            if visited[i] == 0:  # If city is not visited, it starts a new province
                num_prov += 1
                dfs(i)  # Perform DFS to mark all connected cities

        return num_prov  # Return the total number of provinces

from typing import List
from collections import deque, defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Finds the minimum number of roads that need to be reordered so that 
        every city can reach city 0.
        
        Parameters:
        n (int): The number of cities.
        connections (List[List[int]]): List of directed roads as [from, to].
        
        Returns:
        int: The minimum number of roads that must be reordered.
        """
        graph = defaultdict(list)

        # Convert edge list into adjacency list representation
        for u, v in connections:
            graph[u].append((v, 1))  # Original direction
            graph[v].append((u, 0))  # Reverse direction (does not need reordering)
        
        queue = deque([0])  # Start BFS from city 0
        visited = set([0])
        reorder_count = 0

        # Perform BFS
        while queue:
            city = queue.popleft()
            for neighbor, needs_reorder in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    reorder_count += needs_reorder  # Count roads that need to be reordered
        
        return reorder_count

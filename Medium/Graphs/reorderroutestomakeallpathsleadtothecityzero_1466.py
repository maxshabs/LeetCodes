# Solution for LeetCode Problem 1466: Reorder Routes to Make All Paths Lead to the City Zero
# Time Complexity: O(N), where N is the number of cities (nodes).
#   - We iterate over the roads once to build the adjacency list (O(N)).
#   - We perform a BFS traversal, visiting each city once (O(N)).
# Space Complexity: O(N), as we store the adjacency list, visited set, and BFS queue.

from typing import List
from collections import deque, defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        Finds the minimum number of roads that need to be reordered so that 
        every city can reach city 0.

        Parameters:
        n (int): The number of cities.
        connections (List[List[int]]): List of directed roads represented as [from, to].

        Returns:
        int: The minimum number of roads that must be reordered.
        """
        # Step 1: Build an adjacency list with road direction tracking
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  # Original direction (needs reordering)
            graph[v].append((u, 0))  # Reverse direction (does not need reordering)

        # Step 2: Initialize BFS
        queue = deque([0])  # Start BFS from city 0
        visited = set([0])  # Track visited cities
        reorder_count = 0  # Count of roads that need to be reordered

        # Step 3: Perform BFS traversal
        while queue:
            city = queue.popleft()
            for neighbor, needs_reorder in graph[city]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    reorder_count += needs_reorder  # Count roads that need to be reordered

        return reorder_count  # Return the total number of reversed roads

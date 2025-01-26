# Solution for LeetCode Problem 332: Reconstruct Itinerary
# Time Complexity: O(E * log(E)), where E is the number of tickets. Sorting the tickets dominates the runtime.
# Space Complexity: O(V + E), where V is the number of airports (vertices) and E is the number of tickets (edges).

from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create a graph where each airport points to a list of destinations.
        # Sort tickets in reverse lexicographical order to enable efficient popping from the list.
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        # Initialize the stack with the starting airport "JFK"
        stack = ["JFK"]
        result = []
        
        # Perform a depth-first search (DFS) using the stack
        while stack:
            # If the current airport has more destinations, keep exploring
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            # Otherwise, add the current airport to the result and backtrack
            else:
                result.append(stack.pop())
        
        # Reverse the result to obtain the itinerary in the correct order
        return result[::-1]

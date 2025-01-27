# Solution for LeetCode Problem 1548: Minimum Cost to Connect All Points
# Time Complexity: O(N^2 * logN), where N is the number of points.
#   - Constructing the distance list takes O(N^2).
#   - Each operation in the priority queue takes O(logN), and in the worst case, we process O(N^2) edges.
# Space Complexity: O(N^2), for storing the graph representation (distance dictionary).

import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create a dictionary to store the distances from each point to all other points
        dist = {}
        n = len(points)
        for i in range(n):
            dist[i] = []
        
        # Calculate the Manhattan distance between all pairs of points
        for i in range(n):
            x1, y1 = points[i]
            for j in range(n):
                if i == j: 
                    continue  # Skip the same point
                x2, y2 = points[j]
                cur_dist = abs(x1 - x2) + abs(y1 - y2)
                dist[i].append((j, cur_dist))  # Append (neighbor index, distance)
        
        # Use a min-heap to store the current shortest edges
        min_heap = [(0, 0)]  # (distance, point_index), starting from the first point
        visited = set()  # Set to track visited points
        result = 0  # Store the total cost
        
        # Perform Prim's algorithm to connect all points with minimum cost
        while min_heap:
            distance, index = heapq.heappop(min_heap)  # Get the edge with the smallest distance
            if index in visited:
                continue  # Skip if the point has already been visited
            visited.add(index)  # Mark the point as visited
            result += distance  # Add the distance to the total cost
            
            # Push all edges from the current point to the min-heap
            for nei_index, w in dist[index]:
                if nei_index not in visited:
                    heapq.heappush(min_heap, (w, nei_index))
        
        return result  # Return the minimum cost to connect all points

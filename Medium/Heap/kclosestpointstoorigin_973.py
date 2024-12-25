# Solution for LeetCode Problem 973: K Closest Points to Origin
# Time Complexity:
# - O(n + k log n): O(n) for heapify and O(k log n) for extracting the k closest points.
# Space Complexity: O(n), for storing the heap.
from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0, 0) based on Euclidean distance.

        :param points: List of points, where each point is represented as [x, y].
        :param k: Number of closest points to return.
        :return: A list of the k closest points to the origin.
        """
        # Transform the points into a list of tuples with the squared distance and coordinates
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            points[i] = (x ** 2 + y ** 2, x, y)
        
        # Heapify the points based on their distance
        heapq.heapify(points)
        
        result = []
        
        # Extract the k closest points from the heap
        while k:
            current_point = heapq.heappop(points)
            result.append([current_point[1], current_point[2]])
            k -= 1
            
        return result

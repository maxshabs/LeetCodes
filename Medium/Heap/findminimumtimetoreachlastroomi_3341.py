# Solution for LeetCode Problem 3341: Minimum Time to Visit a Cell in a Grid
# Time Complexity: O(n * m * log(n * m)), where n and m are the grid dimensions
# Space Complexity: O(n * m), for the dp table and priority queue

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        min_time_heap = []  # Min-heap for Dijkstra's algorithm: (time, row, col)
        n = len(moveTime)
        m = len(moveTime[0])
        
        # dp[row][col] = shortest time known to reach (row, col)
        dp = [[float('inf')] * m for _ in range(n)]
        heapq.heappush(min_time_heap, (0, 0, 0))  # Start from top-left corner at time 0
        
        # Movement directions: down, right, up, left
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while min_time_heap:
            cur_time, row, col = heapq.heappop(min_time_heap)
            
            # If a shorter path to this cell has already been found, skip
            if cur_time >= dp[row][col]:
                continue

            # Reached the bottom-right corner
            if row == n - 1 and col == m - 1:
                return cur_time

            # Update the best known time to reach this cell
            dp[row][col] = cur_time

            # Try all 4 directions
            for dir_row, dir_col in directions:
                nei_row = row + dir_row
                nei_col = col + dir_col

                # Skip out-of-bounds neighbors
                if not (0 <= nei_row < n and 0 <= nei_col < m):
                    continue

                # Only push if we find a faster way to the neighbor
                if dp[nei_row][nei_col] > cur_time:
                    # Wait if moveTime is higher than current time; otherwise, step immediately
                    time = max(moveTime[nei_row][nei_col], cur_time) + 1
                    heapq.heappush(min_time_heap, (time, nei_row, nei_col))

        # If destination is unreachable
        return -1

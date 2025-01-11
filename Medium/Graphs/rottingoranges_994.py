# Solution for LeetCode Problem 994: Rotting Oranges
# Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the grid.
# Space Complexity: O(n * m), for storing the rotten queue and auxiliary space during BFS.

from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        
        rotten_queue = deque()
        fresh = 0
        time_passed = 0
        
        # Initialize fresh orange count and enqueue all initially rotten oranges
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    rotten_queue.append((row, col))
        
        # BFS to propagate the rotting effect
        while rotten_queue:
            if fresh == 0:
                return time_passed
            
            q_len = len(rotten_queue)
            for i in range(q_len):
                cur_row, cur_col = rotten_queue.popleft()
                # Check and infect adjacent cells
                if cur_row + 1 < num_rows and grid[cur_row + 1][cur_col] == 1:
                    grid[cur_row + 1][cur_col] = 2
                    fresh -= 1
                    rotten_queue.append((cur_row + 1, cur_col))
                if cur_row - 1 >= 0 and grid[cur_row - 1][cur_col] == 1:
                    grid[cur_row - 1][cur_col] = 2
                    fresh -= 1
                    rotten_queue.append((cur_row - 1, cur_col))
                if cur_col + 1 < num_cols and grid[cur_row][cur_col + 1] == 1:
                    grid[cur_row][cur_col + 1] = 2
                    fresh -= 1
                    rotten_queue.append((cur_row, cur_col + 1))
                if cur_col - 1 >= 0 and grid[cur_row][cur_col - 1] == 1:
                    grid[cur_row][cur_col - 1] = 2
                    fresh -= 1
                    rotten_queue.append((cur_row, cur_col - 1))
            
            time_passed += 1
        
        # Return -1 if there are still fresh oranges
        return -1 if fresh > 0 else time_passed

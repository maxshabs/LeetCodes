# Solution for LeetCode Problem 1926: Nearest Exit from Entrance in Maze
# Time Complexity: O(M × N), where M is the number of rows and N is the number of columns.
#   - Each cell is visited at most once in BFS.
# Space Complexity: O(M × N), as we store visited cells in a set.

from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """
        Finds the shortest path from the entrance to the nearest exit in a maze.

        Parameters:
        maze (List[List[str]]): A 2D grid representing the maze, where:
            - '.' represents an open path.
            - '+' represents a wall.
        entrance (List[int]): The starting position in the maze [row, col].

        Returns:
        int: The number of steps to the nearest exit, or -1 if no exit is reachable.
        """
        # Step 1: Initialize BFS
        x_start, y_start = entrance
        q = deque([[x_start, y_start, 0]])  # Store (row, col, steps)
        visited = set()
        m, n = len(maze), len(maze[0])

        # Step 2: Perform BFS to find the nearest exit
        while q:
            x, y, path_len = q.popleft()

            # Step 3: Bounds check
            if x < 0 or y < 0 or x >= m or y >= n:
                continue
            if maze[x][y] == "+" or (x, y) in visited:
                continue

            # Step 4: Exit condition (must not be the entrance)
            if (x == 0 or y == 0 or x == m - 1 or y == n - 1) and [x, y] != entrance:
                return path_len  # Return the number of steps taken

            # Step 5: Mark the cell as visited and explore four directions
            visited.add((x, y))    
            q.append([x + 1, y, path_len + 1])  # Move down
            q.append([x - 1, y, path_len + 1])  # Move up
            q.append([x, y + 1, path_len + 1])  # Move right
            q.append([x, y - 1, path_len + 1])  # Move left
            
        return -1  # No exit found

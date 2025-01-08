# Problem 200: Number of Islands
# Time Complexity: O(N * M) where N is the number of rows and M is the number of columns.
# Space Complexity: O(N * M) in the worst case due to recursion stack size.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in a 2D grid using Depth First Search (DFS).
        
        :param grid: 2D list representing the map with '1' as land and '0' as water.
        :return: The total number of islands.
        """
        num_rows, num_cols = len(grid), len(grid[0])  # Dimensions of the grid
        islands = 0  # Counter for the number of islands
        
        def dfs(row: int, col: int) -> None:
            """
            Perform DFS to mark all parts of the current island as visited.
            
            :param row: Current row in the grid.
            :param col: Current column in the grid.
            """
            # Base case: Check if the cell is out of bounds or is water
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[row][col] == "0":
                return
            
            # Mark the current cell as visited
            grid[row][col] = "0"
            
            # Explore all four directions
            dfs(row - 1, col)  # Up
            dfs(row + 1, col)  # Down
            dfs(row, col - 1)  # Left
            dfs(row, col + 1)  # Right
        
        # Traverse the grid
        for row in range(num_rows):
            for col in range(num_cols):
                # If a cell is land ('1'), increment the island count and start a DFS
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        
        return islands

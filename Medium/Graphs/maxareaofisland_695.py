# Solution for LeetCode Problem 695: Max Area of Island
# Time Complexity: O(m * n), where m is the number of rows and n is the number of columns in the grid.
# Space Complexity: O(m * n), due to the recursion stack in the worst case if the island covers the entire grid.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Calculates the maximum area of an island in a given grid. An island is defined as a group of 
        connected '1's (land) surrounded by water ('0'). The connection can be horizontal or vertical.

        :param grid: 2D list representing the grid where '1' is land and '0' is water.
        :return: The area of the largest island.
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        max_island = 0

        def dfs(row: int, col: int) -> int:
            """
            Depth First Search to calculate the area of an island starting from a given cell.

            :param row: Current row index.
            :param col: Current column index.
            :return: The area of the island connected to the starting cell.
            """
            # Base case: Check boundaries and if the cell is water or already visited
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols or grid[row][col] == 0:
                return 0

            # Mark the cell as visited
            grid[row][col] = 0

            # Recursively calculate the area of the island
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:  # Found a new island
                    max_island = max(max_island, dfs(row, col))

        return max_island

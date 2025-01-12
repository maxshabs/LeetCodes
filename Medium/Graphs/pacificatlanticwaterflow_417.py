# Solution for LeetCode Problem 417: Pacific Atlantic Water Flow
# Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the grid. 
#                  Each cell is visited at most once for the Pacific and once for the Atlantic.
# Space Complexity: O(n * m), due to the storage required for the visited sets and the recursion stack.

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific_set, atlantic_set = set(), set()
        result = []
        
        def dfs(row: int, col: int, cur_set: set, prev_height):
            if row < 0 or row == num_rows or col < 0 or col == num_cols or (row, col) in cur_set or prev_height > heights[row][col]:
                return
            
            cur_set.add((row, col))

            dfs(row + 1, col, cur_set, heights[row][col])
            dfs(row - 1, col, cur_set, heights[row][col])
            dfs(row, col + 1, cur_set, heights[row][col])
            dfs(row, col - 1, cur_set, heights[row][col])
        
        # Traverse the grid for Pacific and Atlantic borders
        for row in range(num_rows):
            dfs(row, 0, pacific_set, heights[row][0])  # Left column (Pacific)
            dfs(row, num_cols - 1, atlantic_set, heights[row][num_cols - 1])  # Right column (Atlantic)
        
        for col in range(num_cols):
            dfs(0, col, pacific_set, heights[0][col])  # Top row (Pacific)
            dfs(num_rows - 1, col, atlantic_set, heights[num_rows - 1][col])  # Bottom row (Atlantic)
        
        # Collect cells that can flow to both oceans
        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in pacific_set and (row, col) in atlantic_set:
                    result.append([row, col])
        
        return result

# Solution for LeetCode Problem 130: Surrounded Regions
# Time Complexity: O(n * m), where n is the number of rows and m is the number of columns in the board.
#                  Each cell is visited at most once during the DFS traversal.
# Space Complexity: O(n * m), due to the storage of visited and reachable_o sets, and the recursion stack.

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()
        reachable_o = set()

        # Depth First Search to mark reachable 'O's
        def dfs(row: int, col: int):
            if row == num_rows or col == num_cols or row < 0 or col < 0 or (row, col) in visited:
                return
            
            visited.add((row, col))
            
            if board[row][col] == "O":
                reachable_o.add((row, col))
            else:
                return

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Perform DFS from all boundary 'O's
        for col in range(num_cols):
            if board[0][col] == "O":
                dfs(0, col)
            if board[num_rows - 1][col] == "O":
                dfs(num_rows - 1, col)
        
        for row in range(num_rows):
            if board[row][0] == "O":
                dfs(row, 0)
            if board[row][num_cols - 1] == "O":
                dfs(row, num_cols - 1)

        # Update the board: flip unreached 'O's to 'X's
        for row in range(num_rows):
            for col in range(num_cols):
                if board[row][col] == "O" and (row, col) not in reachable_o:
                    board[row][col] = "X"

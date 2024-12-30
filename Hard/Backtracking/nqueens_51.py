# Solution for LeetCode Problem 51: N-Queens
# Time Complexity: O(n!), where N is the size of the board.
# Space Complexity: O(n), for auxiliary sets and recursion stack.

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solves the N-Queens problem, finding all possible ways to place N queens 
        on an n x n chessboard such that no two queens attack each other.

        :param n: The size of the chessboard (n x n).
        :return: A list of all valid configurations, where each configuration is 
                 represented as a list of strings.
        """
        result = []  # Stores all valid solutions
        pos_diag = set()  # Positive diagonals (row + col)
        neg_diag = set()  # Negative diagonals (row - col)
        columns = set()   # Columns with queens placed

        current_combination = []  # Stores the current board configuration

        def recursive(row_num: int):
            """
            Backtracking function to explore all valid board configurations.
            
            :param row_num: Current row to place a queen.
            """
            # Base case: All rows processed, store the solution
            if row_num >= n:
                result.append(current_combination.copy())
                return
            
            # Try placing a queen in each column of the current row
            for col in range(n):
                # Skip invalid placements
                if col in columns or row_num + col in pos_diag or row_num - col in neg_diag:
                    continue
                
                # Construct the current row string with a queen at the selected column
                cur_str = ''.join("Q" if i == col else "." for i in range(n))
                
                # Update sets and current configuration
                current_combination.append(cur_str)
                pos_diag.add(row_num + col)
                neg_diag.add(row_num - col)
                columns.add(col)
                
                # Recurse to the next row
                recursive(row_num + 1)
                
                # Backtrack: Remove the queen and reset constraints
                current_combination.pop()
                pos_diag.remove(row_num + col)
                neg_diag.remove(row_num - col)
                columns.remove(col)

        # Start the recursive backtracking from the first row
        recursive(0)
        return result

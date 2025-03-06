# Solution for LeetCode Problem 2352: Equal Row and Column Pairs
# Time Complexity: O(N^2), where N is the number of rows (or columns) in the grid.
#   - Constructing the row frequency dictionary takes O(N).
#   - Iterating through columns and checking in the dictionary takes O(N^2).
# Space Complexity: O(N^2), as we store at most N rows in the dictionary.

from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """
        Counts the number of pairs where a row in the grid matches a column.

        Parameters:
        grid (List[List[int]]): A square matrix of integers.

        Returns:
        int: The number of equal row and column pairs.
        """
        pairs_counter = 0  # Tracks the number of matching row-column pairs
        rows_dict = {}  # Dictionary to store row frequency

        # Store each row as a tuple in the dictionary with its count
        for row in grid:
            row_tuple = tuple(row)  # Convert row to tuple (hashable type)
            rows_dict[row_tuple] = rows_dict.get(row_tuple, 0) + 1

        # Iterate over columns by transposing the grid using zip(*grid)
        for col in zip(*grid):  # zip(*grid) extracts columns as tuples
            if col in rows_dict:
                pairs_counter += rows_dict[col]  # Add the count of matching rows

        return pairs_counter  # Return the total number of matching pairs

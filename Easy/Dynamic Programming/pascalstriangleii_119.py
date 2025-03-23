# Solution for LeetCode Problem 119: Pascal's Triangle II
# Time Complexity: O(N^2), where N is the given row index.
#   - We compute each element of each row up to rowIndex.
# Space Complexity: O(N), for storing only the current row.

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Returns the rowIndex-th row (0-indexed) of Pascal's Triangle.

        In Pascal's Triangle:
        - The first and last elements of each row are 1.
        - Each inner element is the sum of the two elements above it.

        Parameters:
        rowIndex (int): The index of the row to generate.

        Returns:
        List[int]: The rowIndex-th row of Pascal's Triangle.
        """
        # Initialize the first row
        prev = cur = [1]

        # Build each row up to the desired rowIndex
        for i in range(1, rowIndex + 1):
            prev = cur  # Save previous row
            cur = [1] * (i + 1)  # Start new row with 1s at both ends
            # Fill in inner elements using values from the previous row
            for j in range(1, i):
                cur[j] = prev[j - 1] + prev[j]

        return cur  # Return the final row

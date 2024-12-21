# Solution for LeetCode Problem 74: Search a 2D Matrix
# Time Complexity: O(log(m) + log(n)), where m is the number of rows and n is the number of columns.
#   - The first binary search over the rows takes O(log(m)).
#   - The second binary search over the columns takes O(log(n)).
# Space Complexity: O(1), as no additional space is used apart from variables.

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search to identify the row containing the target
        lower, upper = 0, len(matrix) - 1
        row_index = -1  # Variable to store the index of the row where the target might exist

        while lower <= upper:
            middle = (upper + lower) // 2

            # If the target is less than the first element of the middle row, search in upper rows
            if target < matrix[middle][0]:
                upper = middle - 1

            # If the target is greater than the last element of the middle row, search in lower rows
            elif target > matrix[middle][-1]:
                lower = middle + 1

            # Target is within the range of the current row
            else:
                row_index = middle
                break

        # If no valid row is found, return False
        if row_index == -1:
            return False

        # Binary search within the identified row
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            middle = (left + right) // 2

            # If the target is less than the middle element, search in the left half
            if target < matrix[row_index][middle]:
                right = middle - 1

            # If the target is greater than the middle element, search in the right half
            elif target > matrix[row_index][middle]:
                left = middle + 1

            # If the target is found, return True
            else:
                return True

        # Return False if the target is not found
        return False

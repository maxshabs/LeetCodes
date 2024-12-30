# Solution for LeetCode Problem 79: Word Search
# Time Complexity: O(m * n * 4^L), where m and n are the number of rows and columns in the board, and L is the length of the word.
# - In the worst case, each cell can trigger a recursive exploration in 4 directions for each character in the word.
# Space Complexity: O(n), due to the recursion stack and the `visited` set, which stores the path being explored.

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determines if a given word exists in a 2D board, where the word must be constructed 
        from letters in adjacent cells (vertically or horizontally), and the same cell cannot
        be used more than once in a single word.

        :param board: A 2D list of characters representing the board.
        :param word: A string representing the word to search for.
        :return: True if the word exists in the board, otherwise False.
        """
        num_rows = len(board)
        num_cols = len(board[0])
        visited = set()  # Tracks visited cells during the current word search.

        def recursive(row, col, i) -> bool:
            """
            Backtracking function to explore the board recursively to match the word.

            :param row: Current row in the board.
            :param col: Current column in the board.
            :param i: Current index in the word being matched.
            :return: True if the word can be constructed from the current position, otherwise False.
            """
            # Base case: If all characters in the word are matched
            if i == len(word):
                return True

            # Boundary conditions and character match check
            if (
                row < 0 or row >= num_rows or
                col < 0 or col >= num_cols or
                word[i] != board[row][col] or
                (row, col) in visited
            ):
                return False

            # Mark the cell as visited
            visited.add((row, col))

            # Explore all possible directions: down, up, right, left
            result = (
                recursive(row + 1, col, i + 1) or
                recursive(row - 1, col, i + 1) or
                recursive(row, col + 1, i + 1) or
                recursive(row, col - 1, i + 1)
            )

            # Backtrack: unmark the cell as visited
            visited.remove((row, col))
            return result

        # Start the search from every cell in the board
        for row in range(num_rows):
            for col in range(num_cols):
                if recursive(row, col, 0):
                    return True
        return False

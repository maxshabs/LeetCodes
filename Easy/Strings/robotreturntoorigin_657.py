# Solution for LeetCode Problem 657: Robot Return to Origin
# Time Complexity: O(n), where n is the length of the input string `moves`.
# - Each character in the string is processed once.
# Space Complexity: O(1), as only a few integer variables are used for counting.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Determines if a sequence of moves will return the robot to the origin point (0, 0).

        The moves are represented as characters:
        - 'U' (up): Increases the vertical position.
        - 'D' (down): Decreases the vertical position.
        - 'L' (left): Increases the horizontal position.
        - 'R' (right): Decreases the horizontal position.

        :param moves: A string of moves.
        :return: True if the moves bring the robot back to the origin, otherwise False.
        """
        # Initialize counters for vertical and horizontal movements
        up_down_count = 0
        left_right_count = 0

        # Iterate through each move and update the respective counters
        for char in moves:
            if char == 'U':  # Move up
                up_down_count += 1
            elif char == 'D':  # Move down
                up_down_count -= 1
            elif char == 'L':  # Move left
                left_right_count += 1
            elif char == 'R':  # Move right
                left_right_count -= 1

        # Check if both horizontal and vertical movements cancel out
        return left_right_count == 0 and up_down_count == 0

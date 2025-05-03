# Solution for LeetCode Problem 1007: Minimum Domino Rotations For Equal Row
# Time Complexity: O(6 * n) = O(n), where n is the length of the input arrays
# Space Complexity: O(1), since only a few variables are used

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        result = n + 1  # Start with an impossible high number (max rotations + 1)

        # Try each possible domino face value (1 to 6) as the candidate to unify the row
        for value in range(1, 7):
            top_swaps = 0     # Number of swaps needed in tops to make all values == value
            bot_swaps = 0     # Number of swaps needed in bottoms to make all values == value
            is_valid = True   # Flag to check if it's possible to align all to this value

            # Check all domino positions
            for top, bottom in zip(tops, bottoms):
                # If neither top nor bottom has the candidate value, alignment is impossible
                if top != value and bottom != value:
                    is_valid = False
                    break

                # Count how many swaps would be needed in each row
                if top != value:
                    top_swaps += 1
                if bottom != value:
                    bot_swaps += 1

            # If this value can align the row, update the minimum result
            if is_valid:
                result = min(result, top_swaps, bot_swaps)

        # If result wasn't updated, no valid alignment was found
        return -1 if result == n + 1 else result

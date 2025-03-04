# Solution for LeetCode Problem 1732: Find the Highest Altitude
# Time Complexity: O(N), where N is the length of gain.
#   - We iterate through the gain array once.
# Space Complexity: O(1), as we use only a few extra variables.

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Finds the highest altitude reached after following the given gain values.

        Parameters:
        gain (List[int]): A list of integers representing altitude changes.

        Returns:
        int: The maximum altitude reached.
        """
        max_alt = 0  # Tracks the highest altitude reached
        curr_alt = 0  # Current altitude, initialized at 0

        # Iterate through the altitude changes
        for g in gain:
            curr_alt += g  # Update current altitude
            max_alt = max(max_alt, curr_alt)  # Update the highest altitude if needed

        return max_alt  # Return the highest altitude reached

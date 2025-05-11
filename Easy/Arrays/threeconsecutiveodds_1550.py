# Solution for LeetCode Problem 1550: Three Consecutive Odds
# Time Complexity: O(n), where n is the length of the input array
# Space Complexity: O(1), uses only a counter for tracking

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0  # Tracks number of consecutive odd numbers

        for num in arr:
            if not num % 2:
                count = 0  # Reset if number is even
                continue
            count += 1

            if count == 3:
                return True  # Found three consecutive odds

        return False  # Did not find any such triplet

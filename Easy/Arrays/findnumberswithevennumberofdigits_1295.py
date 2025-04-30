# Solution for LeetCode Problem 1295: Find Numbers with Even Number of Digits
# Time Complexity: O(n), where n is the number of elements in nums
# Space Complexity: O(1), using only a constant counter

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0  # Count of numbers with even number of digits

        for num in nums:
            # Convert number to string and check if digit count is even
            if not len(str(num)) % 2:
                result += 1

        return result

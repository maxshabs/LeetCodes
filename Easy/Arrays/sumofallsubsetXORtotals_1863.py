# Solution for LeetCode Problem 1863: Sum of All Subset XOR Totals
# Time Complexity: O(N), where N is the length of the input list `nums`.
#   - We iterate once through the array and perform bitwise operations.
# Space Complexity: O(1), as only a few variables are used.

from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_or = 0

        # Step 1: Calculate the bitwise OR of all elements to capture all active bits
        for num in nums:
            total_or |= num

        # Step 2: Multiply by 2^(n-1), since each bit contributes to half the subsets
        return total_or * (2 ** (len(nums) - 1))

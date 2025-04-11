# Solution for LeetCode Problem 2843: Count Symmetric Integers
# Time Complexity: O(N * D), where N is the size of the range (high - low + 1),
# and D is the number of digits in each number (max 6).
# Space Complexity: O(D), for string and digit operations.

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        sym_count = 0

        # Iterate through all numbers in the range
        for i in range(low, high + 1):
            s = str(i)

            # Only consider numbers with even digit length
            if len(s) % 2 != 0:
                continue

            mid = len(s) // 2

            # Check if sum of left half digits == sum of right half digits
            if sum(map(int, s[:mid])) == sum(map(int, s[mid:])):
                sym_count += 1

        return sym_count

# Solution for LeetCode Problem 2145: Count the Hidden Sequences
# Time Complexity: O(n), where n is the length of the differences list
# Space Complexity: O(1), using constant space with running variables

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        diff_sum = 0               # Running total to simulate prefix sums
        min_val, max_val = 0, 0    # Track the min and max values of the reconstructed array

        # Build prefix sum and track min/max
        for diff in differences:
            diff_sum += diff
            max_val = max(max_val, diff_sum)
            min_val = min(min_val, diff_sum)

        # The entire reconstructed sequence must fit within [lower, upper]
        # Shifting the whole array up/down is allowed via its starting value
        return max(0, (upper - lower + 1) - (max_val - min_val))

# Solution for LeetCode Problem 790: Domino and Tromino Tiling
# Time Complexity: O(n), where n is the length of the board
# Space Complexity: O(n), for the dynamic programming array

class Solution:
    def numTilings(self, n: int) -> int:
        # Handle base cases directly
        if n == 0 or n == 1:
            return 1

        MOD = 10**9 + 7  # Use modulo to prevent integer overflow

        # Initialize DP array where dp[i] = number of tilings for 2×i board
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty board
        dp[1] = 1  # One vertical domino
        dp[2] = 2  # Two verticals or two horizontals

        # Apply recurrence relation:
        # dp[i] = 2 * dp[i - 1] + dp[i - 3]
        # Explanation:
        # - 2 * dp[i - 1]: one vertical domino or two horizontals
        # - dp[i - 3]: new tromino placement on top of a 2×(i-3) board
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD

        return dp[-1]

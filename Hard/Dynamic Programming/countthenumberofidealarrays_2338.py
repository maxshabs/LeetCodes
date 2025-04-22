# Solution for LeetCode Problem 2338: Count the Number of Ideal Arrays
# Time Complexity: O(maxValue * m + n), where m = min(n, 14)
# Space Complexity: O(maxValue * m), due to the DP table

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        m = min(n, 14)  # The max depth of sequences is capped at 14 due to factor limits
        mod = 10 ** 9 + 7

        # dp[x][k] = number of sequences of length k ending with x (where each next is a multiple)
        dp = [[0] * (m + 1) for _ in range(maxValue + 1)]

        # Initialize sequences of length 1
        for i in range(1, maxValue + 1):
            dp[i][1] = 1
            j = 2
            # For each i, fill in its multiples i*j
            while i * j < maxValue + 1:
                for k in range(1, m):
                    dp[i * j][k + 1] += dp[i][k]
                j += 1

        # Precompute factorials and inverse factorials for combinations (n choose k)
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % mod

        inverted_fact = [1] * n
        inverted_fact[n - 1] = pow(fact[n - 1], mod - 2, mod)
        for i in range(n - 2, -1, -1):
            inverted_fact[i] = inverted_fact[i + 1] * (i + 1) % mod

        res = 0
        fact_n = fact[n - 1]

        # For each sequence of length j ending with i,
        # calculate number of ways to place that sequence in array of size n
        for i in range(1, maxValue + 1):
            for j in range(1, m + 1):
                if dp[i][j] > 0:
                    # Number of ways to insert a sequence of length j in array of size n
                    num_ways = fact_n * inverted_fact[j - 1] % mod * inverted_fact[n - j] % mod
                    res = (res + dp[i][j] * num_ways) % mod

        return res

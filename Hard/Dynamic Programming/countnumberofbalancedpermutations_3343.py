# Solution for LeetCode Problem 3343: Count Balanced Permutations
# Time Complexity: O(n^2 * sum_digits), where n is the length of num and sum_digits is the total digit sum
# Space Complexity: O(n * sum_digits), due to the dynamic programming table

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        total = sum(int(c) for c in num)

        # If the total sum of digits is odd, it's impossible to split into two equal halves
        if total % 2:
            return 0

        # Precompute factorials and inverse factorials for combination calculations
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i % MOD

        inverse = [1] * (n + 1)
        for i in range(2, n + 1):
            inverse[i] = MOD - (MOD // i) * inverse[MOD % i] % MOD

        inverse_factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            inverse_factorial[i] = inverse_factorial[i - 1] * inverse[i] % MOD

        target = total // 2
        half_len = n // 2

        # dp[s][k] = number of ways to pick k digits from num whose sum is s
        dp = [[0] * (half_len + 1) for _ in range(target + 1)]
        dp[0][0] = 1

        digits_freq = [0] * 10

        for c in num:
            digit = int(c)
            digits_freq[digit] += 1

            # Update dp table in reverse to avoid overcounting
            for s in range(target, digit - 1, -1):
                for k in range(half_len, 0 , -1):
                    dp[s][k] = (dp[s][k] + dp[s - digit][k - 1]) % MOD

        # Ways to pick half the digits that sum to target
        result = dp[target][half_len]

        # Multiply by ways to arrange each half (factorials), then divide by duplicates
        result = result * factorial[half_len] % MOD * factorial[n - half_len] % MOD
        for count in digits_freq:
            result = result * inverse_factorial[count] % MOD

        return result

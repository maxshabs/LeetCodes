# Solution for LeetCode Problem 2999: Count the Number of Powerful Integers
# Time Complexity: O(D), where D is the number of digits in `finish`.
#   - The DP table has D rows and 2 columns, processed once for each of two bounds.
# Space Complexity: O(D), for the dynamic programming table.

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def count_powerful_up_to(num: int) -> int:
            num_str = str(num)
            suffix_len = len(s)
            prefix_len = len(num_str) - suffix_len

            # If num is too small to hold the suffix, return 0
            if prefix_len < 0:
                return 0

            # dp[i][tight] means:
            # - i is the current index in the prefix part of the number
            # - tight = 0: we are building a number strictly less than the prefix of num
            # - tight = 1: we are building a number equal to the prefix of num so far
            dp = [[0] * 2 for _ in range(prefix_len + 1)]

            # Extract the suffix of num and compare with s
            suffix_from_num = num_str[prefix_len:]

            # Base case: At the end of the prefix, we must ensure the suffix condition is met
            dp[prefix_len][0] = 1  # Any number formed so far is valid
            dp[prefix_len][1] = 1 if suffix_from_num >= s else 0  # Valid only if suffix ≥ s

            # Fill dp from back to front
            for i in range(prefix_len - 1, -1, -1):
                digit = int(num_str[i])

                # If already less than prefix, can choose any digit [0, limit]
                dp[i][0] = (limit + 1) * dp[i + 1][0]

                # If still matching prefix, digits must be ≤ current digit in num_str
                if digit <= limit:
                    # For digits less than current → go to loose state
                    dp[i][1] = digit * dp[i + 1][0] + dp[i + 1][1]  # last digit equals → stay tight
                else:
                    # All digits ≤ limit are allowed
                    dp[i][1] = (limit + 1) * dp[i + 1][0]

            return dp[0][1]

        # Count powerful integers in range [start, finish] by inclusion-exclusion
        return count_powerful_up_to(finish) - count_powerful_up_to(start - 1)

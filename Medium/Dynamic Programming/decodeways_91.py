# Solution for LeetCode Problem 91: Decode Ways
# Time Complexity: O(n), where n is the length of the string `s`.
# Space Complexity: O(n), due to the `dp` dictionary used to store intermediate results.

from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Determines the number of ways to decode a string `s` where:
        - '1' -> 'A', ..., '26' -> 'Z'.

        :param s: The input string consisting of digits.
        :return: The number of possible decoding ways.
        """
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and 0 <= int(s[i + 1]) <= 6)):
                dp[i] += dp[i + 2]
        return dp[0]

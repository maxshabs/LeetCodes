# Solution for LeetCode Problem 3335: Length of Transformed String After t Operations
# Time Complexity: O(t + n), where t is the number of transformations and n is the length of string s
# Space Complexity: O(t), for the dynamic programming table

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        # dp[i] = total number of characters generated after i transformations starting from 'a'
        dp = [0] * (26 + t)
        
        # Base case: with 0 to 25 transformations, each letter is still 1 character
        for i in range(26):
            dp[i] = 1

        # Recurrence: 
        # dp[i] = dp[i - 26] (for when 'z' splits to 'a' + 'b') + 
        #         dp[i - 25] (for when a non-'z' letter shifts forward)
        for i in range(26, 26 + t):
            dp[i] = (dp[i - 26] + dp[i - 25]) % MOD

        result = 0

        # For each character in the input string, apply t transformations
        # and sum the resulting lengths using the dp array
        for c in s:
            index = ord(c) - ord('a') + t
            result = (result + dp[index]) % MOD

        return result

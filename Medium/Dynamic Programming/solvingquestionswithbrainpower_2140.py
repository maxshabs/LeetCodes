# Solution for LeetCode Problem 2140: Solving Questions With Brainpower
# Time Complexity: O(N), where N is the number of questions.
#   - Each question is processed once.
# Space Complexity: O(N), for storing the dynamic programming table.

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n  # dp[i] stores the max points starting from question i
        dp[n - 1] = questions[n - 1][0]  # Base case: last question earns its own points

        # Process from the second-last question down to the first
        for index in range(n - 2, -1, -1):
            points, brainpower = questions[index]
            next_index = index + brainpower + 1  # Jump past the brainpower skip

            # Option 1: Solve this question
            solve = points + (dp[next_index] if next_index < n else 0)
            # Option 2: Skip this question
            skip = dp[index + 1]

            # Take the better of the two options
            dp[index] = max(solve, skip)

        return dp[0]  # The answer is the max points from index 0

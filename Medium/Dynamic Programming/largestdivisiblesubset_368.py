# Solution for LeetCode Problem 368: Largest Divisible Subset
# Time Complexity: O(N^2), where N is the length of the input list `nums`.
#   - For each pair of indices (i, j), we check divisibility and potentially update dp.
# Space Complexity: O(N^2), since we're storing subsets in dp.

from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()  # Sort to ensure smaller elements come first, making divisibility easier to check
        n = len(nums)

        # dp[i] holds the largest divisible subset that ends with nums[i]
        dp = [[num] for num in nums]

        for i in range(n):
            for j in range(i):
                # If nums[i] is divisible by nums[j] and extending dp[j] would make a longer subset
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    # Extend the subset ending at j by adding nums[i]
                    dp[i] = dp[j] + [nums[i]]

        # Return the longest subset found
        return max(dp, key=len)

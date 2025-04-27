# Solution for LeetCode Problem 3392: Count the Number of Special Subarrays
# Time Complexity: O(n), where n is the length of nums
# Space Complexity: O(1), using only a counter

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        # Start from index 2 because we are checking triplets (i-2, i-1, i)
        for i in range(2, len(nums)):
            # Check if the middle element is the average of the two outer elements
            if 2 * (nums[i - 2] + nums[i]) == nums[i - 1] * 2:
                count += 1

        return count

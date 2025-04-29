# Solution for LeetCode Problem 2962: Count Subarrays Where Max Element Appears at Least K Times
# Time Complexity: O(n), where n is the length of nums (each element is visited at most twice)
# Space Complexity: O(1), using only constant extra space

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)  # Find the maximum value in the array
        result = 0           # Store the final count of valid subarrays
        left = 0             # Left boundary of the sliding window
        count = 0            # Count of how many times max_val appears in the current window
        n = len(nums)

        for right, val in enumerate(nums):
            # Expand the window by including nums[right]
            if val == max_val:
                count += 1

            # Shrink the window from the left while max_val appears at least k times
            while count == k:
                # All subarrays starting from 'left' and ending at or after 'right' are valid
                result += n - right
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return result

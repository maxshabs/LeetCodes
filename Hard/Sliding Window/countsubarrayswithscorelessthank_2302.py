# Solution for LeetCode Problem 2302: Count Subarrays With Score Less Than K
# Time Complexity: O(n), where n is the length of nums (each element is visited at most twice)
# Space Complexity: O(1), using only a few pointers and variables

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0           # Total number of valid subarrays
        sum = 0             # Sum of current sliding window
        left = 0            # Left boundary of the sliding window

        for right in range(len(nums)):
            sum += nums[right]  # Expand the window by adding the current element

            # Shrink the window from the left until score < k
            while sum * (right - left + 1) >= k:
                sum -= nums[left]
                left += 1

            # Add the number of valid subarrays ending at 'right'
            count += (right - left) + 1

        return count

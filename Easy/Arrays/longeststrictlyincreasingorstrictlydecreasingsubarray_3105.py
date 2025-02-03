# Solution for LeetCode Problem 3105: Longest Monotonic Subarray
# Time Complexity: O(N), where N is the length of the array.
#   - We iterate through the array once to track the longest increasing or decreasing subarray.
# Space Complexity: O(1), as we use only a few extra variables.

from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 1  # Stores the maximum length of a monotonic subarray found
        cur_dec = 1  # Tracks the length of the current decreasing subarray
        cur_inc = 1  # Tracks the length of the current increasing subarray

        # Iterate through the array to check increasing and decreasing sequences
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:  # If the current number is smaller, it's a decreasing sequence
                cur_dec += 1
                cur_inc = 1  # Reset increasing count
            elif nums[i - 1] < nums[i]:  # If the current number is larger, it's an increasing sequence
                cur_inc += 1
                cur_dec = 1  # Reset decreasing count
            else:  # If the numbers are equal, reset both counters
                cur_inc = 1
                cur_dec = 1

            # Update the maximum length found
            longest = max(longest, cur_dec, cur_inc)

        return longest  # Return the longest monotonic subarray length

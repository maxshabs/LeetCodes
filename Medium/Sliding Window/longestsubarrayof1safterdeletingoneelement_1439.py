# Solution for LeetCode Problem 1439: Longest Subarray of 1's After Deleting One Element
# Time Complexity: O(N), where N is the length of nums.
#   - We traverse the array once using a sliding window approach.
# Space Complexity: O(1), as we use only a few extra variables.

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Finds the length of the longest contiguous subarray of 1's after deleting exactly one element.

        Parameters:
        nums (List[int]): A list of integers (0s and 1s).

        Returns:
        int: The length of the longest subarray of 1's after one deletion.
        """
        longest = 0  # Stores the maximum length of the subarray found
        left = 0  # Left pointer for the sliding window
        zero_count = 0  # Counts the number of zeros in the window
        length = len(nums)

        # Sliding window approach
        for right in range(length):
            if nums[right] == 0:
                zero_count += 1  # Track zeros in the window

            # If we have more than one zero, adjust the left pointer to maintain validity
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Shrink the window

            # Update the longest valid subarray length (excluding the one deleted zero)
            longest = max(longest, right - left + 1 - zero_count)

        # If the longest subarray is equal to the entire array, we must delete one element
        if longest == length:
            longest -= 1

        return longest  # Return the maximum valid subarray length

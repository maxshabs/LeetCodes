# Solution for LeetCode Problem 724: Find Pivot Index
# Time Complexity: O(N), where N is the length of nums.
#   - We iterate through the array twice: once to compute right_sum and once to check pivot index.
# Space Complexity: O(1), as we use only a few extra variables.

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Finds the pivot index where the sum of elements to the left is equal to the sum of elements to the right.

        Parameters:
        nums (List[int]): A list of integers.

        Returns:
        int: The leftmost pivot index if found, otherwise -1.
        """
        left_sum, right_sum = 0, 0

        # Compute the total sum of the array, excluding the first element
        for i in range(1, len(nums)):
            right_sum += nums[i]

        # Check if the first element is the pivot index
        if left_sum == right_sum:
            return 0

        # Iterate through the array to find the pivot index
        for i in range(1, len(nums)):
            left_sum += nums[i - 1]  # Add previous element to left_sum
            right_sum -= nums[i]  # Remove current element from right_sum
            
            if left_sum == right_sum:  # Check for pivot condition
                return i

        return -1  # Return -1 if no pivot index is found

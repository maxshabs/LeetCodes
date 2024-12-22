# Solution for LeetCode Problem 33: Search in Rotated Sorted Array
# Time Complexity: O(log n), where n is the length of the input array `nums`
#   - The binary search reduces the search space by half in each iteration.
# Space Complexity: O(1), as no additional space is used apart from a few variables.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            middle = (left + right) // 2

            # If the target is found at the middle, return its index
            if target == nums[middle]:
                return middle

            # Check if the left half of the array is sorted
            if nums[left] <= nums[middle]:
                # If the target lies within the sorted left half, narrow the search to the left half
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                # Otherwise, narrow the search to the right half
                else:
                    left = middle + 1
            # If the right half of the array is sorted
            else:
                # If the target lies within the sorted right half, narrow the search to the right half
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                # Otherwise, narrow the search to the left half
                else:
                    right = middle - 1

        # Return -1 if the target is not found
        return -1

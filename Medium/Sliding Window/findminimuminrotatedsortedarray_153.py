# Solution for LeetCode Problem 153: Find Minimum in Rotated Sorted Array
# Time Complexity: O(log n), where n is the length of the input array `nums`
#   - The binary search reduces the search space by half in each iteration.
# Space Complexity: O(1), as no additional space is used apart from a few variables.

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1

        # Perform binary search
        while left <= right:
            # Calculate the middle index
            middle = (left + right) // 2

            # If the middle element is greater than the last element, the minimum is in the right half
            if nums[middle] > nums[-1]:
                left = middle + 1

            # If the middle element is less than or equal to the last element, it might be the minimum
            elif nums[middle] <= nums[-1]:
                # Check if the middle element is the first element or less than its previous element
                if middle == 0 or nums[middle] < nums[middle - 1]:
                    return nums[middle]
                else:
                    # If not, the minimum is in the left half
                    right = middle - 1

# Solution for LeetCode Problem 1752: Check if Array is Sorted and Rotated
# Time Complexity: O(N), where N is the length of the array.
#   - We iterate through the array once to find the pivot point.
#   - Another pass checks if the remaining elements form a sorted sequence.
# Space Complexity: O(1), as we use only a few extra variables.

from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        i = 0
        # Find the first decreasing pair, which indicates the rotation point
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1
        
        # If no rotation point is found, the array is already sorted
        if i == len(nums) - 1:
            return True
        
        # Move to the next element after the rotation point
        i += 1
        
        # Check if the remaining elements form a sorted sequence
        for k in range(len(nums) - 1):
            if nums[(i + k) % len(nums)] > nums[(i + k + 1) % len(nums)]:
                return False  # The array is not sorted and rotated correctly
        
        return True  # The array is a valid rotated sorted array

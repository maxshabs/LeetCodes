# Solution for LeetCode Problem 2563: Count the Number of Fair Pairs
# Time Complexity: O(n log n), due to sorting and two-pointer scans
# Space Complexity: O(1), excluding sorting space

from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()  # Sort the array to allow two-pointer processing

        upper_bound_count = 0
        left = 0
        right = len(nums) - 1

        # Count number of pairs (i, j) with i < j and nums[i] + nums[j] <= upper
        while left < right:
            if nums[left] + nums[right] <= upper:
                # All indices from left+1 to right form valid pairs with left
                upper_bound_count += (right - left)
                left += 1
            else:
                right -= 1

        lower_bound_count = 0
        left = 0
        right = len(nums) - 1

        # Count number of pairs (i, j) with i < j and nums[i] + nums[j] < lower
        while left < right:
            if nums[left] + nums[right] < lower:
                # All indices from left+1 to right form invalid pairs with left (less than lower)
                lower_bound_count += (right - left)
                left += 1
            else:
                right -= 1

        # The number of fair pairs is the difference between the two bounds
        return upper_bound_count - lower_bound_count

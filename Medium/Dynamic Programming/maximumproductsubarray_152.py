# Solution for LeetCode Problem 152: Maximum Product Subarray
# Time Complexity: O(n), where n is the length of the input array `nums`.
# Space Complexity: O(1), as we use only a constant amount of additional space.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the maximum product of a contiguous subarray within the given array.

        :param nums: A list of integers (both positive and negative).
        :return: The maximum product of any contiguous subarray.
        """
        # Initialize result with the first element
        result = nums[0]
        # Track the current maximum and minimum products
        cur_max, cur_min = 1, 1
        
        # Traverse through the array
        for num in nums:
            # Temporary values for the current minimum and maximum calculations
            min_calc = cur_min * num
            max_calc = cur_max * num
            # Update the current maximum product
            cur_max = max(min_calc, max_calc, num)
            # Update the current minimum product
            cur_min = min(min_calc, max_calc, num)
            # Update the global result with the largest product seen so far
            result = max(result, cur_max)
            
        return result

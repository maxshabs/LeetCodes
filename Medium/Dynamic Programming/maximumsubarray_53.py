# Solution for LeetCode Problem 53: Maximum Subarray
# Time Complexity: O(n), where n is the length of the input array. We traverse the array once.
# Space Complexity: O(1), as the solution uses only constant extra space.

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize the current sum and the maximum subarray sum
        sum = 0
        max_sub = nums[0]
        
        # Iterate through the array
        for n in nums:
            # Reset the current sum to 0 if it becomes negative
            if sum < 0:
                sum = 0
            # Add the current number to the current sum
            sum += n
            # Update the maximum subarray sum
            max_sub = max(max_sub, sum)
        
        # Return the maximum subarray sum
        return max_sub

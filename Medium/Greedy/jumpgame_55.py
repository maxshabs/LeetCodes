# Solution for LeetCode Problem 55: Jump Game
# Time Complexity: O(n), where n is the length of the input array. We traverse the array once in reverse.
# Space Complexity: O(1), as the solution uses only constant extra space.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        # Initialize the target index to the last position
        target = len_nums - 1
        
        # Traverse the array from the second-to-last element to the first
        for i in range(len_nums - 2, -1, -1):
            # Check if the current index can reach or surpass the target
            if i + nums[i] >= target:
                target = i  # Update the target to the current index
        
        # Return True if the target index reaches 0, indicating the start can reach the end
        return target == 0

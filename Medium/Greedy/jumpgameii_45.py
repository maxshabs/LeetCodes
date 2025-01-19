# Solution for LeetCode Problem 45: Jump Game II
# Time Complexity: O(n^2), where n is the length of the input array. 
# In the worst case, for every range, the inner loop iterates over the range, resulting in quadratic complexity.
# Space Complexity: O(1), as the solution uses only constant extra space.

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        # Initialize pointers for the current range (left and right) and number of jumps
        left = right = 0
        len_nums = len(nums)
        jumps = 0
        
        # Continue until the end of the array is reached
        while right < len_nums - 1:
            # Calculate the farthest point reachable in the current range
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            
            # Update pointers for the next range and increment the jump counter
            left = right + 1
            right = farthest
            jumps += 1
        
        # Return the total number of jumps needed
        return jumps

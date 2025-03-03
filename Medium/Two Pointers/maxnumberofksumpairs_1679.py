# Solution for LeetCode Problem 1679: Max Number of K-Sum Pairs
# Time Complexity: O(N log N), where N is the length of nums.
#   - Sorting takes O(N log N).
#   - The two-pointer approach runs in O(N).
# Space Complexity: O(1), as we sort the array in place and use only a few extra variables.

from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array to use the two-pointer technique
        i, j = 0, len(nums) - 1  # Two pointers: one at the start, one at the end
        num_operations = 0  # Counter for valid pairs

        while i < j:
            pair_sum = nums[i] + nums[j]  # Compute the sum of the current pair
            if pair_sum == k:
                num_operations += 1  # A valid pair is found
                i += 1  # Move the left pointer forward
                j -= 1  # Move the right pointer backward
            elif pair_sum < k:
                i += 1  # Increase the sum by moving the left pointer forward
            else:
                j -= 1  # Decrease the sum by moving the right pointer backward
        
        return num_operations  # Return the total number of k-sum pairs found

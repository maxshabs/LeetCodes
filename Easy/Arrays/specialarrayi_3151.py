# Solution for LeetCode Problem 3151: Check if an Array is Special
# Time Complexity: O(N), where N is the length of the array.
#   - We iterate through the array once to check adjacent elements.
# Space Complexity: O(1), as we use only a few extra variables.

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # If the array has only one element, it is trivially special.
        if len(nums) == 1:
            return True
        
        # Iterate through the array, checking the parity of adjacent elements.
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:  # If two consecutive elements have the same parity
                return False  # The array is not special
        
        return True  # The array is special

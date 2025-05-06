# Solution for LeetCode Problem 1920: Build Array from Permutation
# Time Complexity: O(n), where n is the length of the input array
# Space Complexity: O(1), in-place transformation without using extra arra

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # First pass: encode both original and new value into each element
        # New value to store is nums[nums[i]], encoded as: original + (new_value % n) * n
        for i in range(n):
            nums[i] += (nums[nums[i]] % 1000) * 1000  # 1000 is safe since 0 <= nums[i] < n <= 1000

        # Second pass: extract the new value by dividing by 1000
        for i in range(n):
            nums[i] //= 1000

        return nums

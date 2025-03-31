# Solution for LeetCode Problem 2206: Divide Array Into Equal Pairs
# Time Complexity: O(N), where N is the number of elements in `nums`.
#   - Each element is inserted and removed from the set at most once.
# Space Complexity: O(N), for the set storing unmatched elements.

from typing import List

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_set = set()

        # For each number, add it to the set if it's not there,
        # or remove it if it's already been seen once (forming a pair).
        for num in nums:
            if num in nums_set:
                nums_set.discard(num)  # Second occurrence, remove to form a pair
            else:
                nums_set.add(num)  # First occurrence, add to set

        # If the set is empty, all numbers formed valid pairs
        return not len(nums_set)

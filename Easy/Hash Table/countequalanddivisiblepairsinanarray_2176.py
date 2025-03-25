# Solution for LeetCode Problem 2176: Count Equal and Divisible Pairs in an Array
# Time Complexity: O(N^2) in the worst case (when all values are equal),
#   - But more efficient in practice due to hashing.
# Space Complexity: O(N), where N is the number of elements in nums (for storing indices in the hash map).

from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        Counts the number of index pairs (i, j) such that:
        - nums[i] == nums[j]
        - i < j
        - (i * j) is divisible by k

        Parameters:
        nums (List[int]): The list of integers.
        k (int): The divisor.

        Returns:
        int: The total number of valid pairs.
        """
        num_pairs = 0
        d = defaultdict(list)  # Map from number to list of its indices

        # Iterate through the list and track indices of each number
        for i, num in enumerate(nums):
            # For each previous index with the same value, check the divisibility condition
            if num in d:
                for index in d[num]:
                    if (i * index) % k == 0:
                        num_pairs += 1
            d[num].append(i)  # Store the current index for future matches

        return num_pairs

from collections import defaultdict
from typing import List

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        Problem 2176: Count Equal and Divisible Pairs in an Array
        Time Complexity: O(n^2) in worst case if many duplicates exist
        Space Complexity: O(n) for storing indices of each number

        Args:
            nums (List[int]): List of integers
            k (int): Divisor for the condition (i * j) % k == 0

        Returns:
            int: Number of valid index pairs (i, j)
        """

        num_pairs = 0  # Counter for valid pairs
        d = defaultdict(list)  # Dictionary to store indices for each value in nums

        # Iterate over nums with their indices
        for i, num in enumerate(nums):
            # If the current number has been seen before
            if num in d:
                # Check all previously stored indices for this number
                for index in d[num]:
                    # Check if i * index is divisible by k
                    if (i * index) % k == 0:
                        num_pairs += 1

            # Store the current index for future comparisons
            d[num].append(i)

        return num_pairs

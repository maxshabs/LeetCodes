# Solution for LeetCode Problem 78: Subsets
# Time Complexity: O(2^n), where n is the number of elements in the input list `nums`.
# - For each element, there are two choices: include it in the subset or exclude it.
# - This results in 2^n subsets in total.
# Space Complexity: O(n), where n is the depth of the recursion stack and the size of the current subset.

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible subsets (the power set) of a given list of distinct integers.

        :param nums: List of distinct integers.
        :return: List of all subsets of the input list `nums`.
        """
        result = []  # Stores all generated subsets
        current_nums = []  # Tracks the current subset being generated

        def recursive(i: int):
            """
            Recursive helper function to generate subsets by exploring inclusion
            and exclusion of the current element.

            :param i: Current index in the input list `nums`.
            """
            # Base case: If the index exceeds the list length, append the current subset to results
            if i >= len(nums):
                result.append(current_nums.copy())  # Add a copy of the current subset
                return

            # Include nums[i] in the current subset and recurse
            current_nums.append(nums[i])
            recursive(i + 1)

            # Exclude nums[i] from the current subset and recurse
            current_nums.pop()
            recursive(i + 1)

        # Start the recursion with the first element
        recursive(0)

        # Return the list of all subsets
        return result

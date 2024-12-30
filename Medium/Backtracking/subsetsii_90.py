# Solution for LeetCode Problem 90: Subsets II
# Time Complexity: O(2^n), where n is the number of elements in the input array. Each element can either be included or excluded.
# Space Complexity: O(n), due to the space used by the recursion stack and the current combination list.

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique subsets of the input array, including duplicates.
        
        :param nums: List of integers, which may contain duplicates.
        :return: A list of all unique subsets.
        """
        result = []  # List to store all unique subsets
        nums.sort()  # Sort the array to handle duplicates

        def recursive(i: int, comb: List[int]):
            """
            Backtracking function to explore all possible subsets.

            :param i: Current index in the nums list.
            :param comb: Current subset being built.
            """
            # Base case: If all elements have been processed, add the subset to results.
            if i == len(nums):
                result.append(comb.copy())
                return
            
            # Include the current element in the subset.
            comb.append(nums[i])
            recursive(i + 1, comb)
            comb.pop()  # Backtrack to explore subsets without the current element.
            
            # Skip duplicates to ensure unique subsets.
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # Explore subsets without including the current element.
            recursive(i + 1, comb)
        
        # Start the recursive exploration from index 0 with an empty subset.
        recursive(0, [])
        return result

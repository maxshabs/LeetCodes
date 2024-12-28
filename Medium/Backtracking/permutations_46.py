# Solution for LeetCode Problem 46: Permutations
# Time Complexity: O(n!), where n is the number of elements in nums. There are n! permutations, and each one takes O(n) to construct.
# Space Complexity: O(n!), due to the space required to store all permutations in the result.

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generates all possible permutations of the given list of numbers.
        
        :param nums: List of distinct integers.
        :return: A list of lists, where each inner list represents a unique permutation.
        """
        result = []  # Stores all generated permutations
        
        # Base case: if nums is empty, return a list with an empty list
        if len(nums) == 0:
            return [[]]
        
        # Recursive step: generate permutations for nums[1:] (all elements except the first)
        perms = self.permute(nums[1:])
        
        # For each permutation in perms, insert nums[0] at all possible positions
        for perm in perms:
            for i in range(len(perm) + 1):  # +1 to insert at the end of the list
                # Create a new permutation by inserting nums[0] at index i
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                result.append(perm_copy)
        
        return result

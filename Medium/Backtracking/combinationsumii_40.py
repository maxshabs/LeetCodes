# Solution for LeetCode Problem 40: Combination Sum II
# Time Complexity: O(2^n), where n is the number of candidates. In the worst case, every subset of candidates is explored.
# Space Complexity: O(n), due to the space used by the recursion stack and the current combination list.

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates where the chosen numbers sum to the target.
        Each number in candidates may only be used once in the combination.

        :param candidates: List of integers, where some elements may appear more than once.
        :param target: The target sum for combinations.
        :return: A list of lists, where each inner list represents a unique combination of numbers summing to the target.
        """
        candidates.sort()  # Sort to help identify duplicates and ensure unique combinations.
        result_arr = []  # List to store all unique combinations.

        def recurcive(i: int, sum: int, comb: List[int]):
            """
            Backtracking function to explore all possible combinations.

            :param i: Current index in the candidates list.
            :param sum: Current sum of the elements in the combination.
            :param comb: Current combination being built.
            """
            # If the current sum equals the target, add the combination to the results.
            if sum == target:
                result_arr.append(comb.copy())
                return

            # If the current sum exceeds the target or we've exhausted candidates, stop further exploration.
            if i == len(candidates) or sum > target:
                return
            
            # Include the current candidate and explore further.
            comb.append(candidates[i])
            recurcive(i + 1, sum + candidates[i], comb)
            comb.pop()  # Backtrack by removing the last added candidate.

            # Skip over duplicate candidates to avoid duplicate combinations.
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # Explore without including the current candidate.
            recurcive(i + 1, sum, comb)
            
        # Start the recursive exploration.
        recurcive(0, 0 , [])
        return result_arr

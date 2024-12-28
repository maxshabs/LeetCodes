# Solution for LeetCode Problem 39: Combination Sum
# Time Complexity: O(2^n), where n is the number of candidates. The recursion explores all possible subsets.
# Space Complexity: O(target), due to the space used by the recursion stack and the current combination list.

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations of candidates where the chosen numbers sum to the target.

        Each number in candidates may be used an unlimited number of times in a combination.

        :param candidates: List of distinct integers.
        :param target: The target sum for combinations.
        :return: A list of lists, where each inner list represents a unique combination of numbers summing to target.
        """
        result = []  # Stores all valid combinations
        cur_candidates = []  # Temporary list to store the current combination
        
        def recursive(i, sum):
            """
            Backtracking function to explore all possible combinations.
            
            :param i: Current index in the candidates list.
            :param sum: Current sum of the elements in cur_candidates.
            """
            # Base case: if the current sum exceeds the target or all candidates are explored
            if sum > target or i >= len(candidates):
                return
            
            # Base case: if the current sum equals the target, save the combination
            if sum == target:
                result.append(cur_candidates.copy())
                return
            
            # Include the current candidate and continue
            cur_candidates.append(candidates[i])
            recursive(i, sum + candidates[i])
            
            # Backtrack: exclude the current candidate and explore the next one
            cur_candidates.pop()
            recursive(i + 1, sum)
        
        # Start the recursive exploration from index 0 and sum 0
        recursive(0, 0)
        
        return result

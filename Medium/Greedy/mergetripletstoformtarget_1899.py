# Solution for LeetCode Problem 1899: Merge Triplets to Form Target Triplet
# Time Complexity: O(n), where n is the number of triplets in the input list. This is because we iterate through the triplets once.
# Space Complexity: O(1), as we only use a fixed amount of additional space for the `res` list.

from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Initialize a result triplet to track the maximum values we can achieve for each position
        res = [0, 0, 0]
        
        # Iterate through all triplets
        for triplet in triplets:
            # Check if the current triplet satisfies the conditions for the target triplet
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                # Update the result triplet with the maximum values at each position
                res = [
                    max(triplet[0], res[0]),
                    max(triplet[1], res[1]),
                    max(triplet[2], res[2])
                ]
                # If the result triplet matches the target triplet, return True
                if res == target:
                    return True
        
        # If no combination of triplets can form the target, return False
        return False

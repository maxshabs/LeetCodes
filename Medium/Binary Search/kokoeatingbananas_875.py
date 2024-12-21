# Solution for LeetCode Problem 875: Koko Eating Bananas
# Time Complexity: O(n * log(max(piles))), where:
#   - n is the number of piles.
#   - log(max(piles)) is the number of iterations in the binary search.
# Space Complexity: O(1), as no extra space is used apart from variables.

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the search range for `k`
        left, right = 1, max(piles)

        # Variable to store the minimum valid eating speed
        ret_k = right

        # Perform binary search
        while left <= right:
            # Calculate the middle eating speed
            k = (right + left) // 2

            # Calculate the total time needed to eat all bananas at speed `k`
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile / k)

            # If the total time exceeds `h`, increase the eating speed
            if total_time > h:
                left = k + 1
            # Otherwise, decrease the eating speed and update the result
            else:    
                ret_k = k
                right = k - 1
        
        # Return the minimum valid eating speed
        return ret_k

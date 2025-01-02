# Solution for LeetCode Problem 746: Min Cost Climbing Stairs
# Time Complexity: O(n), where n is the length of the cost array. We iterate through the array once.
# Space Complexity: O(1), as we use only two variables (`first` and `second`) to track costs.

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Calculates the minimum cost to climb to the top of the staircase,
        starting at either step 0 or step 1.

        :param cost: A list of integers representing the cost of each step.
        :return: The minimum cost to reach the top of the staircase.
        """
        # Initialize the costs for the first two steps
        first, second = cost[0], cost[1]
        
        # Calculate the minimum cost for each subsequent step
        for i in range(2, len(cost)):
            temp = second  # Temporarily store the previous cost
            second = cost[i] + min(first, second)  # Update with the minimum cost
            first = temp  # Shift the previous cost
        
        # Return the minimum cost to reach the top
        return min(first, second)

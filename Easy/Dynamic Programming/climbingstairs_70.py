# Solution for LeetCode Problem 70: Climbing Stairs
# Time Complexity: O(n), where n is the number of stairs. We iterate through the range from 2 to n.
# Space Complexity: O(1), as only a constant amount of extra space is used.

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb a staircase with n steps,
        where each step can be either 1 or 2 steps at a time.

        :param n: The total number of stairs.
        :return: The number of distinct ways to reach the top.
        """
        # Base cases for 1 or 0 stairs
        first, second = 1, 1
        
        # Iteratively compute the number of ways for each stair
        for i in range(2, n + 1):
            temp = second  # Temporarily store the previous number of ways
            second = first + second  # Update to the new number of ways
            first = temp  # Shift the previous number of ways
        
        return second

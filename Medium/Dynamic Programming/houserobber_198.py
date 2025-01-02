# Solution for LeetCode Problem 198: House Robber
# Time Complexity: O(n), where n is the number of houses (length of the `nums` array).
# Space Complexity: O(1), as only two variables (`first` and `second`) are used for tracking the maximum amount.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Determines the maximum amount of money that can be robbed without alerting the police.
        Adjacent houses cannot be robbed on the same night.

        :param nums: A list of integers representing the amount of money at each house.
        :return: The maximum amount of money that can be robbed.
        """
        # Initialize variables to store the maximum money robbed so far.
        first, second = 0, 0
        
        # Iterate through each house
        for num in nums:
            # Calculate the maximum money robbed if including the current house
            temp = max(second, first + num)
            first = second  # Update `first` to the previous `second`
            second = temp  # Update `second` to the new maximum
        
        # Return the maximum money robbed
        return second

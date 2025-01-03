# Solution for LeetCode Problem 213: House Robber II
# Time Complexity: O(n), where n is the number of houses in the input list.
# Space Complexity: O(1), as only two variables (`first` and `second`) are used for tracking the maximum amount.

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Determines the maximum amount of money that can be robbed from a circular street of houses
        without alerting the police. Adjacent houses cannot be robbed on the same night.

        :param nums: A list of integers representing the amount of money at each house.
        :return: The maximum amount of money that can be robbed.
        """
        # If there's only one house, rob it directly.
        if len(nums) == 1:
            return nums[0]
        
        # Calculate the maximum money by considering:
        # - Robbing houses from index 1 to the last house (nums[1:])
        # - Robbing houses from index 0 to the second-to-last house (nums[:-1])
        # - Robbing only the first house (nums[0]) if there's only one house.
        return max(self.help(nums[1:]), self.help(nums[:-1]))
    
    def help(self, nums: List[int]) -> int:
        """
        Helper function to calculate the maximum money robbed for a linear street of houses.
        
        :param nums: A sublist of the original house list representing a linear street.
        :return: The maximum amount of money that can be robbed.
        """
        first, second = 0, 0  # Initialize variables to track max money robbed up to the previous two houses.
        for i in range(len(nums)):
            # Calculate the max money robbed including or excluding the current house.
            temp = max(first + nums[i], second)
            first = second  # Update `first` to the previous `second`.
            second = temp  # Update `second` to the new maximum.
        
        return second  # Return the maximum money robbed.


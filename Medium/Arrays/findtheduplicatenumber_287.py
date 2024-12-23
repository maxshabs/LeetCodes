# Solution for LeetCode Problem 287: Find the Duplicate Number
# Time Complexity: O(n), where n is the number of elements in the array.
#   - The algorithm effectively traverses the array twice using the Floyd's Tortoise and Hare cycle detection algorithm.
# Space Complexity: O(1), as no additional data structures are used, and only pointers are maintained.

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in an array where each integer is between 1 and n (inclusive), 
        and there is only one repeated number. The algorithm uses constant space and runs in O(n) time.

        :param nums: List[int] - An array containing n+1 integers where each integer is between 1 and n.
        :return: int - The duplicate number in the array.
        """
        # Initialize two pointers, both starting at the first index
        slow = fast = 0

        # Step 1: Detect the cycle using Floyd's Tortoise and Hare algorithm
        while True:
            slow = nums[slow]             # Move `slow` one step forward
            fast = nums[nums[fast]]       # Move `fast` two steps forward
            if slow == fast:              # If the two pointers meet, a cycle is detected
                break

        # Step 2: Find the entrance of the cycle, which corresponds to the duplicate number
        slow2 = 0
        while True:
            slow = nums[slow]             # Move `slow` one step forward
            slow2 = nums[slow2]           # Move `slow2` one step forward
            if slow == slow2:             # When the two pointers meet again, it's the duplicate number
                return slow

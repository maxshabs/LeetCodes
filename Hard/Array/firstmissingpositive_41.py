# Solution for LeetCode Problem 41: First Missing Positive
# Time Complexity: O(n), where n is the length of the input list `nums`.
# - The first loop iterates through all elements to filter positive numbers: O(n).
# - The second loop marks indices corresponding to numbers in the filtered list: O(n).
# - The final loop checks for the first positive index in the filtered list: O(n).
# Space Complexity: O(n), due to the use of an additional list `non_negative_nums` to store positive numbers.

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Finds the smallest missing positive integer in an unsorted array.
        
        :param nums: List of integers.
        :return: The smallest missing positive integer.
        """
        # Step 1: Filter out non-positive numbers
        non_negative_nums = []
        for num in nums:
            if num > 0:
                non_negative_nums.append(num)
        
        # Step 2: Mark indices corresponding to numbers in the filtered list
        for num in non_negative_nums:
            index = abs(num) - 1  # Calculate the zero-based index
            if index < len(non_negative_nums) and non_negative_nums[index] > 0:
                non_negative_nums[index] *= -1  # Mark as visited by negating the value
        
        # Step 3: Find the first positive index
        for index, num in enumerate(non_negative_nums):
            if num > 0:  # First unmarked index corresponds to the missing number
                return index + 1
        
        # Step 4: If all indices are marked, return the next positive integer
        return len(non_negative_nums) + 1

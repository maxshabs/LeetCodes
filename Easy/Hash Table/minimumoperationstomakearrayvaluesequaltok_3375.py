# Solution for LeetCode Problem 3375: Minimum Number of Operations to Make Array values Equal to K
# Time Complexity: O(N), where N is the length of the input list `nums`
# Space Complexity: O(N), due to use of a set to store unique numbers

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_num = min(nums)  # Find the smallest number in the array

        # If k is greater than the smallest number, it is impossible to achieve it with replacements
        if k > min_num:
            return -1

        unique_numbers = set(nums)  # Store all unique numbers in the array

        # If min_num == k, we may already have one correct number, reduce count by 1
        return len(unique_numbers) - (1 if min_num == k else 0)

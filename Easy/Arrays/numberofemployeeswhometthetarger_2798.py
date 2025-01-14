# Solution for LeetCode Problem 2798: Number of Employees Who Met the Target
# Time Complexity: O(n), where n is the length of the `hours` list. 
#                  The generator expression iterates over the `hours` list once.
# Space Complexity: O(1), as the generator expression does not require additional memory for storage.

from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for i in range(len(hours)) if hours[i] >= target)

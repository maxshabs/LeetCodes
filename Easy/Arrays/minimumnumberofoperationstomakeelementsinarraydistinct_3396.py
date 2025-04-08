# Solution for LeetCode Problem 3396: Minimum Operations to Exceed Threshold Value I
# Time Complexity: O(N), where N is the length of the input list `nums`
# Space Complexity: O(1), since the boolean array is fixed at size 100

from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        arr = [False] * 100  # To track which numbers have already been seen
        for i in range(len(nums) - 1, -1, -1):
            if arr[nums[i] - 1]:
                # If we encounter a duplicate, we return the minimal operation count
                return (i + 3) // 3
            arr[nums[i] - 1] = True

        # If all elements are unique, no operations are needed
        return 0

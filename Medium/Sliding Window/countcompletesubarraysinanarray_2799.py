# Solution for LeetCode Problem 2799: Count Complete Subarrays in an Array
# Time Complexity: O(n), where n is the length of nums — each element is processed at most twice (sliding window)
# Space Complexity: O(k), where k is the number of distinct elements in nums

from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = 0

        # Step 1: Determine the number of distinct elements in the entire array
        distinct = set(nums)
        num_distinct = len(distinct)

        # Step 2: Use a sliding window to count subarrays with all distinct elements
        cur_dist = defaultdict(int)  # Tracks the frequency of elements in the current window
        j = 0  # Left pointer of the sliding window

        for i in range(len(nums)):
            cur_dist[nums[i]] += 1

            # When the current window contains all distinct elements
            while len(cur_dist) == num_distinct:
                # All subarrays from current i to the end are valid
                count += (len(nums) - i)

                # Shrink the window from the left
                cur_dist[nums[j]] -= 1
                if cur_dist[nums[j]] == 0:
                    del cur_dist[nums[j]]
                j += 1

        return count

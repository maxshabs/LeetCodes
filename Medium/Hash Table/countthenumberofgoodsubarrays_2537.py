# Solution for LeetCode Problem 2537: Count the Number of Good Subarrays
# Time Complexity: O(n), where n is the length of `nums`
#   - Each element is added and removed from the window at most once
# Space Complexity: O(n), for the hashmap storing frequency counts

from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0                     # Left end of the sliding window
        count = {}                   # Frequency map of elements in the current window
        pairs_num = 0                # Number of good pairs (nums[i] == nums[j]) in the current window
        good_sub = 0                 # Total number of good subarrays found

        for right in range(len(nums)):
            # Add nums[right] to the window and update pair count
            count[nums[right]] = count.get(nums[right], 0) + 1
            pairs_num += count[nums[right]] - 1  # Every new same-value adds new pairs

            # Shrink window from the left while we have enough pairs
            while pairs_num >= k:
                # All subarrays from current left to end that start at left are good
                good_sub += len(nums) - right

                # Remove nums[left] from window and update pair count
                count[nums[left]] -= 1
                pairs_num -= count[nums[left]]  # Removing reduces number of pairs
                left += 1

        return good_sub

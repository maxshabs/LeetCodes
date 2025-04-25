# Solution for LeetCode Problem 2845: Count of Interesting Subarrays
# Time Complexity: O(n), where n is the length of the input list `nums`
# Space Complexity: O(modulo), to store frequency counts for each modulo class

from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = 0                      # Final result: count of interesting subarrays
        cur_prefix_sum = 0           # Running count of elements where num % modulo == k
        modulo_dict = defaultdict(int)
        modulo_dict[0] = 1           # Base case: one way to start with a sum that satisfies the condition

        for num in nums:
            # Step 1: Check if this number satisfies the interesting condition
            if num % modulo == k:
                cur_prefix_sum += 1  # Count how many such elements we've seen so far

            # Step 2: Compute the current prefix sum modulo
            cur_mod = cur_prefix_sum % modulo

            # Step 3: Find how many previous prefix sums had (prefix_sum % modulo == (cur_mod - k + modulo) % modulo)
            # This ensures that the count of interesting elements in the subarray % modulo == k
            remaining = (cur_mod - k + modulo) % modulo
            res += modulo_dict[remaining]

            # Step 4: Record the current modulo class
            modulo_dict[cur_mod] += 1

        return res

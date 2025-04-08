# Solution for LeetCode Problem 2542: Maximum Subsequence Score
# Time Complexity: O(N log N), where N is the length of nums1/nums2.
#   - Sorting takes O(N log N)
#   - Each heap operation is O(log K), and performed at most N times.
# Space Complexity: O(K), for maintaining a min-heap of at most K elements.

import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        max_sub = 0          # Stores the maximum score found so far
        cur_sum = 0          # Running sum of the selected nums1 values
        min_heap = []        # Min-heap to maintain the k largest nums1 values

        # Step 1: Zip and sort by nums2 descending to fix the minimum nums2 in the score
        for num1, num2 in sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True):
            heapq.heappush(min_heap, num1)  # Include current num1 in the heap
            cur_sum += num1                 # Add to current sum

            # Step 2: If we've added k elements, calculate the score
            if len(min_heap) == k:
                # num2 is the current minimum in the sorted order
                max_sub = max(max_sub, cur_sum * num2)

                # Step 3: Remove the smallest num1 to prepare for next iteration
                cur_sum -= heapq.heappop(min_heap)

        return max_sub

# Solution for LeetCode Problem 215: Kth Largest Element in an Array
# Time Complexity: O(k + (n - k) * log k), where n is the length of the input array `nums`.
# - Building the heap takes O(k).
# - For each of the remaining (n - k) elements, we perform an O(log k) operation.
# Space Complexity: O(k), for maintaining a heap of size `k`.

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element in an array using a min-heap.
        
        :param nums: List of integers.
        :param k: Integer representing the position of the largest element to find.
        :return: The kth largest element in the array.
        """
        # Step 1: Build a min-heap with the first k elements.
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Step 2: Process the remaining elements in the array.
        for num in nums[k:]:
            # If the current number is larger than or equal to the smallest element in the heap,
            # replace the smallest element with the current number.
            if num >= min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
        
        # Step 3: The root of the heap is the kth largest element.
        return min_heap[0]

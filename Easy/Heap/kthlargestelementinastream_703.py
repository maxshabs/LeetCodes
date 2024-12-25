# Solution for LeetCode Problem 703: Kth Largest Element in a Stream
# Time Complexity:
# - `__init__`: O(n log n), where `n` is the size of the input list `nums`, due to heapify and potential heap pops.
# - `add`: O(log k), where `k` is the size of the heap, for heap operations.
# Space Complexity: O(k), as the heap size is maintained at most `k` elements.

from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the KthLargest object with an integer k and a list of integers nums.
        
        :param k: The kth largest element to maintain in the stream.
        :param nums: Initial list of numbers.
        """
        self.min_heap = nums  # A min-heap to store the largest k elements
        heapq.heapify(self.min_heap)  # Convert the list into a min-heap
        self.k = k  # Target rank of the largest element
        
        # Reduce the heap to at most k elements by removing the smallest elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        """
        Adds a new value to the stream and returns the kth largest element.
        
        :param val: The new value to add.
        :return: The kth largest element in the stream after adding the new value.
        """
        # Add the new value to the min-heap
        heapq.heappush(self.min_heap, val)
        
        # Ensure the heap size does not exceed k
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The root of the heap is the kth largest element
        return self.min_heap[0]

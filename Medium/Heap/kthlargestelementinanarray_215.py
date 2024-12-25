# Solution for LeetCode Problem 215: Kth Largest Element in an Array
# Time Complexity: O(n log k), where n is the length of the input array `nums`.
# - Building the heap takes O(n log k)
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
        # Initialize an empty min-heap
        min_heap = []
        
        # Iterate through the list of numbers
        for num in nums:
            # Add each number to the heap
            heapq.heappush(min_heap, num)
            
            # If the size of the heap exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the heap is the kth largest element
        return min_heap[0]

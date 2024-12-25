# Solution for LeetCode Problem 1046: Last Stone Weight
# Time Complexity:
# - O(n log n), where n is the number of stones, for heap operations.
# Space Complexity: O(n), for storing the heap.

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Simulates the process of smashing stones and returns the weight of the last stone.
        If no stones remain, returns 0.
        
        :param stones: List of integers representing the weights of the stones.
        :return: The weight of the last remaining stone or 0 if no stones are left.
        """
        # Negate the stone weights to simulate a max-heap using Python's heapq (min-heap)
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        # Convert the list into a heap
        heapq.heapify(stones)
        
        # Continue processing until one or no stones are left
        while len(stones) > 1:
            # Extract the two largest stones
            x = abs(heapq.heappop(stones))  # Largest stone
            y = abs(heapq.heappop(stones))  # Second largest stone
            
            # If there is a remainder after smashing, add the difference back to the heap
            if x > y:
                heapq.heappush(stones, y - x)
        
        # If a stone remains, return its absolute weight; otherwise, return 0
        if stones:
            return abs(heapq.heappop(stones))   
        
        return 0

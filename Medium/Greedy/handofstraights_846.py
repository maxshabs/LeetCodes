# Solution for LeetCode Problem 846: Hand of Straights
# Time Complexity: O(n log n), where n is the number of cards in `hand`. This comes from sorting the unique cards using a heap and iterating through the hand.
# Space Complexity: O(n), for storing the count of cards and the heap.

import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If the total number of cards is not divisible by groupSize, it's impossible to divide them into groups
        if len(hand) % groupSize:
            return False
        
        # Count the occurrences of each card
        count = {}
        for card in hand:
            count[card] = 1 + count.get(card, 0)
        
        # Use a min-heap to process cards in ascending order
        min_heap = list(count)
        heapq.heapify(min_heap)
        
        # Try to create groups
        while min_heap:
            cur = min_heap[0]  # Get the smallest card
            for i in range(cur, cur + groupSize):  # Create a group starting from the smallest card
                if i not in count:  # If a required card is missing, return False
                    return False
                count[i] -= 1  # Use one occurrence of the card
                if count[i] == 0:  # If a card is fully used, remove it from the heap
                    if i != min_heap[0]:  # Ensure cards are removed in order
                        return False
                    heapq.heappop(min_heap)
        
        return True

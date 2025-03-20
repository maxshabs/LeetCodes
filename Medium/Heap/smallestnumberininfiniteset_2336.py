# Solution for LeetCode Problem 2336: Smallest Number in Infinite Set
# Time Complexity:
#   - popSmallest(): O(log N) for heap operations.
#   - addBack(): O(log N) for heap insertions.
#   - Initialization is O(1).
# Space Complexity: O(N), where N is the number of removed elements stored in the heap.

import heapq

class SmallestInfiniteSet:
    """
    A class that represents an infinite set of positive integers, supporting operations 
    to fetch the smallest available number and to add back numbers that were previously removed.
    """

    def __init__(self):
        """
        Initializes the infinite set starting from 1.
        - min_num: Tracks the smallest number that has never been removed.
        - s: A set to store numbers that have been added back.
        - heap: A min-heap to efficiently retrieve the smallest available number.
        """
        self.min_num = 1
        self.s = set()
        self.heap = []

    def popSmallest(self) -> int:
        """
        Removes and returns the smallest number from the set.

        Returns:
        int: The smallest available number.

        - If the heap is non-empty, the smallest element from the heap is returned.
        - Otherwise, the next smallest number from min_num is returned.
        """
        if self.heap:
            num = heapq.heappop(self.heap)  # Extract the smallest number from the heap
            self.s.remove(num)  # Remove from the set
            return num

        self.min_num += 1  # Increment min_num to track the next available number
        return self.min_num - 1

    def addBack(self, num: int) -> None:
        """
        Adds back a previously removed number into the set.

        Parameters:
        num (int): The number to be added back.

        - If num is smaller than min_num and not already in the set, add it to the heap.
        - This ensures that numbers added back can be retrieved before min_num.
        """
        if num < self.min_num and num not in self.s:
            self.s.add(num)  # Mark as present
            heapq.heappush(self.heap, num)  # Insert into the heap

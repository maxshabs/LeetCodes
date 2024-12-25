# Solution for LeetCode Problem 295: Find Median from Data Stream
# Time Complexity:
# - `addNum`: O(log n), where n is the number of elements in the heaps. Each insertion or removal operation in a heap takes O(log n).
# - `findMedian`: O(1), as retrieving the top elements of the heaps is constant time.
# Space Complexity: O(n), where n is the total number of elements stored in the heaps.

import heapq

class MedianFinder:
    """
    A data structure that supports efficient addition of numbers and retrieval of the median
    of the numbers in a data stream.
    """

    def __init__(self):
        """
        Initializes two heaps to maintain the two halves of the data stream.
        - `small_nums`: A max-heap (using negative values) to store the smaller half of the numbers.
        - `large_nums`: A min-heap to store the larger half of the numbers.
        """
        self.small_nums = []  # Max-heap (negative values)
        self.large_nums = []  # Min-heap (positive values)

    def addNum(self, num: int) -> None:
        """
        Adds a number to the data structure.

        :param num: The number to add to the data stream.
        """
        # Determine which heap to add the number to
        if self.large_nums and num >= self.large_nums[0]:
            heapq.heappush(self.large_nums, num)
        else:
            heapq.heappush(self.small_nums, num * (-1))  # Use negative for max-heap behavior
        
        # Balance the heaps if their sizes differ by more than 1
        if len(self.large_nums) - len(self.small_nums) > 1:
            val = heapq.heappop(self.large_nums) * (-1)  # Move element from large to small
            heapq.heappush(self.small_nums, val)
        elif len(self.small_nums) - len(self.large_nums) > 0:
            val = heapq.heappop(self.small_nums) * (-1)  # Move element from small to large
            heapq.heappush(self.large_nums, val)

    def findMedian(self) -> float:
        """
        Returns the median of all numbers in the data stream.

        :return: The median as a float.
        """
        # If the total number of elements is odd, return the top of `large_nums` (the larger half)
        if (len(self.large_nums) + len(self.small_nums)) % 2 == 1:
            return self.large_nums[0]
        
        # If even, return the average of the tops of both heaps
        return ((-1) * self.small_nums[0] + self.large_nums[0]) / 2

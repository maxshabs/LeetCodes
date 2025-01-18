# Solution for LeetCode Problem 435: Non-overlapping Intervals
# Time Complexity: O(n log n), where n is the number of intervals. Sorting the intervals takes O(n log n), and the traversal takes O(n).
# Space Complexity: O(1), as the solution only uses a constant amount of extra space.

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their start times
        intervals.sort()
        
        # Initialize the count of overlapping intervals
        count = 0
        
        # Track the end of the previous non-overlapping interval
        prev_end = intervals[0][1]
        
        # Iterate through the intervals starting from the second one
        for interval in intervals[1:]:
            # If there is no overlap with the previous interval
            if prev_end <= interval[0]:
                prev_end = interval[1]  # Update the end to the current interval's end
            else:
                # Increment the count for the overlapping interval
                count += 1
                # Choose the interval with the smaller end to minimize future overlaps
                prev_end = min(prev_end, interval[1])
        
        return count

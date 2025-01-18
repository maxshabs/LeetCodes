# Solution for LeetCode Problem 56: Merge Intervals
# Time Complexity: O(n log n), where n is the number of intervals. Sorting the intervals takes O(n log n), and the single traversal takes O(n).
# Space Complexity: O(n), where n is the number of intervals. This accounts for the result array.

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret_array = []
        
        # Sort the intervals by their start times
        intervals.sort()
        
        # Initialize the previous interval's end to a value smaller than any possible start time
        prev_end = -1
        
        # Traverse the sorted intervals
        for i in range(len(intervals)):
            # If the current interval does not overlap with the previous one
            if prev_end < intervals[i][0]:
                ret_array.append(intervals[i])  # Add the current interval to the result
            else:
                # Merge the intervals by updating the end of the last interval in the result
                ret_array[-1][1] = max(ret_array[-1][1], intervals[i][1])
            
            # Update the previous interval's end
            prev_end = ret_array[-1][1]
        
        return ret_array

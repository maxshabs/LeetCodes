# Solution for LeetCode Problem 57: Insert Interval
# Time Complexity: O(n), where n is the number of intervals in the input list. Each interval is processed once.
# Space Complexity: O(n), where n is the number of intervals in the input list. This accounts for the result array.

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret_arr = []
        len_intervals = len(intervals)
        
        for i in range(len_intervals):
            # If the new interval ends before the current interval starts
            if newInterval[1] < intervals[i][0]:
                ret_arr.append(newInterval)
                return ret_arr + intervals[i:]  # Append newInterval and remaining intervals
            
            # If the new interval starts after the current interval ends
            elif newInterval[0] > intervals[i][1]:
                ret_arr.append(intervals[i])
            
            # Merge overlapping intervals
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
        
        # Append the remaining new interval
        ret_arr.append(newInterval)
        
        return ret_arr

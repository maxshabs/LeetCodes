# Solution for LeetCode Problem 1851: Minimum Interval to Include Each Query
# Time Complexity: O(nlog n + mlog m), where n is the number of intervals and m is the number of queries. 
#                  Sorting the intervals and queries takes O(n log n + m log m), and managing the heap is O((n + m) log n).
# Space Complexity: O(n + m), due to the heap storage and result dictionary.

from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Min-heap to store intervals based on size and ending value
        min_heap = []
        # Dictionary to store results for each query
        result = {}
        # Pointer for iterating through sorted intervals
        i = 0
        # Sort intervals by their starting points
        intervals.sort()
        
        # Process queries in sorted order
        for query in sorted(queries):
            # Push intervals that start before or at the query into the heap
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            # Remove intervals from the heap that end before the query
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            
            # Assign the smallest interval size or -1 if no valid intervals exist
            result[query] = min_heap[0][0] if min_heap else -1
        
        # Retrieve results in the original query order
        res_list = [result[query] for query in queries]

        return res_list

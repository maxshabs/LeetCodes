# Solution for LeetCode Problem 743: Network Delay Time
# Time Complexity: O(n + e * log(n)), where n is the number of nodes and e is the number of edges.
# Space Complexity: O(n + e), for storing the adjacency list and priority queue.

import collections, heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create an adjacency list to represent the graph
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))
        
        # Priority queue to store (time, node)
        nodes = [(0, k)]
        # Set to track visited nodes
        visit = set()
        
        while nodes:
            # Pop the node with the smallest weight
            weight, cur_node = heapq.heappop(nodes)
            
            # If the current node has been visited, skip it
            if cur_node in visit:
                continue
            
            # Mark the current node as visited
            visit.add(cur_node)
            
            # If all nodes have been visited, return the total time
            if len(visit) == n:
                return weight
            
            # Iterate through the neighbors of the current node
            for neighbour, w in edges[cur_node]:
                if neighbour not in visit:
                    heapq.heappush(nodes, (w + weight, neighbour))
        
        # If some nodes are not reachable, return -1
        return -1

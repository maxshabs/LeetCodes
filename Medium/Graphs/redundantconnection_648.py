# Solution for LeetCode Problem 684: Redundant Connection
# Time Complexity: O(n * α(n)), where n is the number of edges, and α(n) is the inverse Ackermann function, which grows very slowly and is almost constant for practical purposes.
# Space Complexity: O(n), due to the storage of the `parents` and `rank` arrays.

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            p = parents[n]
            while p != parents[p]:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p
        
        def union(n1: int, n2: int):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
                
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
# Solution for LeetCode Problem 133: Clone Graph
# Time Complexity: O(V + E), where V is the number of nodes and E is the number of edges in the graph.
# Space Complexity: O(V), due to the storage of the cloned nodes in a dictionary and the recursion stack.

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clones an undirected graph using Depth First Search (DFS).
        
        :param node: A Node object representing the root of the graph.
        :return: A deep copy of the graph's root node.
        """
        if not node:
            return None
        
        cloned = {}  # Dictionary to store the mapping of original nodes to their clones
        
        def dfs(node: Optional['Node']) -> Optional['Node']:
            """
            Recursively clones the graph using DFS.
            
            :param node: The current node being cloned.
            :return: The cloned node corresponding to the current node.
            """
            if node in cloned:
                return cloned[node]  # Return the already cloned node
            
            # Create a copy of the current node
            copy = Node(node.val)
            cloned[node] = copy
            
            # Recursively clone all neighbors
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        return dfs(node)

# Solution for LeetCode Problem 1161: Maximum Level Sum of a Binary Tree
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
#   - Each node is visited once using a level-order traversal (BFS).
# Space Complexity: O(W), where W is the maximum width of the tree.
#   - The queue stores nodes at the deepest level, leading to O(W) space usage.

from typing import Optional
from collections import deque

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Finds the level in the binary tree that has the maximum sum of node values.

        Parameters:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        int: The level (1-indexed) with the highest sum.
        """
        max_sum = root.val  # Initialize max sum with root value
        max_sum_level = 1  # Initialize the level with max sum as 1
        cur_level = 1  # Current level counter
        queue = deque()  # Queue for level-order traversal (BFS)
        
        # Add children of root to the queue
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        
        # Perform BFS traversal
        while queue:
            cur_level += 1
            cur_nodes = []  # Store nodes at the current level
            
            # Dequeue all nodes at the current level
            while queue:
                cur_nodes.append(queue.popleft())
            
            cur_sum = 0  # Sum of values at the current level
            
            # Process all nodes at the current level
            for node in cur_nodes:
                cur_sum += node.val  # Add node value to the sum
                if node.left:
                    queue.append(node.left)  # Add left child to queue
                if node.right:
                    queue.append(node.right)  # Add right child to queue
            
            # Update max sum and corresponding level if needed
            if max_sum < cur_sum:
                max_sum = cur_sum
                max_sum_level = cur_level
        
        return max_sum_level  # Return the level with the highest sum

# Solution for LeetCode Problem 199: Binary Tree Right Side View
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(n), where n is the number of nodes in the binary tree.

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of the nodes visible from the right side of the binary tree.
        
        :param root: Root node of the binary tree.
        :return: A list of integers representing the rightmost node at each level of the tree.
        """
        q = deque()  # Queue for level-order traversal
        if root:
            q.append(root)  # Start the traversal with the root node
            
        rightmost_nodes = []  # List to store the rightmost node values at each level
        
        while q:
            q_len = len(q)  # Number of nodes at the current level
            rightmost = None  # Placeholder for the rightmost node at this level
            
            for i in range(q_len):
                node = q.popleft()  # Dequeue the current node
                rightmost = node  # Update the rightmost node for the current level
                
                # Enqueue the left and right children, if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if rightmost:  # Add the rightmost node's value to the result
                rightmost_nodes.append(rightmost.val)
        
        return rightmost_nodes

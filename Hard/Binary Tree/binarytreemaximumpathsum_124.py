# Solution for LeetCode Problem 124: Binary Tree Maximum Path Sum
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Finds the maximum path sum in a binary tree. A path can start and end at any node.

        :param root: The root node of the binary tree.
        :return: The maximum path sum in the tree.
        """
        self.max_val = float("-inf")  # Variable to store the maximum path sum
        
        def dfs(root: Optional[TreeNode]) -> int:
            """
            Depth-first search helper function to calculate the maximum path sum.
            
            :param root: The current node being processed.
            :return: The maximum sum of a path ending at the current node.
            """
            if not root:  # If the node is null, it contributes 0 to the path
                return 0
            
            # Recursively calculate the maximum path sums for the left and right subtrees
            left_sum = max(0, dfs(root.left))  # Discard negative sums by taking max with 0
            right_sum = max(0, dfs(root.right))  # Discard negative sums by taking max with 0
            
            # Calculate the maximum path sum passing through the current node
            cur_val = root.val + left_sum + right_sum
            
            # Update the global maximum path sum
            self.max_val = max(self.max_val, cur_val)
            
            # Return the maximum path sum ending at the current node
            return root.val + max(left_sum, right_sum)
        
        # Start DFS traversal from the root node
        dfs(root)
        
        # Return the maximum path sum found
        return self.max_val

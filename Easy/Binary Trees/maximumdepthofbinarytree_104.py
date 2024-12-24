# Solution for LeetCode Problem 104: Maximum Depth of Binary Tree
# Time Complexity: O(n), where n is the number of nodes in the binary tree. Each node is visited once.
# Space Complexity: O(h), where h is the height of the binary tree. This accounts for the recursion stack.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the maximum depth of a binary tree.

        :param root: The root node of the binary tree.
        :return: An integer representing the maximum depth of the tree.
        """
        if not root:
            return 0  # If the tree is empty, the depth is 0.

        # Recursively calculate the depth of the left and right subtrees
        # and add 1 for the current node.
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

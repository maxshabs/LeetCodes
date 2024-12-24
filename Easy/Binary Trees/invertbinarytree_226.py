# Solution for LeetCode Problem 226: Invert Binary Tree
# Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited exactly once.
# Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by swapping the left and right subtrees recursively.
        
        :param root: The root node of the binary tree.
        :return: The root node of the inverted binary tree.
        """
        if not root:
            return None  # If the tree is empty, return None.
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the root of the inverted tree
        return root

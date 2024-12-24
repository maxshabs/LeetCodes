# Solution for LeetCode Problem 98: Validate Binary Search Tree
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is a valid binary search tree (BST).
        
        A BST is valid if for every node:
          - All nodes in the left subtree have values less than the node's value.
          - All nodes in the right subtree have values greater than the node's value.
        
        :param root: The root node of the binary tree.
        :return: True if the tree is a valid BST, otherwise False.
        """
        def dfs(root: Optional[TreeNode], lower: int, upper: int) -> bool:
            """
            Depth-first search (DFS) to validate the BST property for all nodes.
            
            :param root: The current node being validated.
            :param lower: The lower bound for the node's value.
            :param upper: The upper bound for the node's value.
            :return: True if the subtree rooted at the current node is a valid BST, otherwise False.
            """
            if not root:  # An empty tree is a valid BST
                return True
            
            # Check if the current node violates the BST property
            if lower >= root.val or root.val >= upper:
                return False
            
            # Recursively validate the left and right subtrees with updated bounds
            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
        
        # Start DFS with initial bounds of negative and positive infinity
        return dfs(root, float("-inf"), float("inf"))

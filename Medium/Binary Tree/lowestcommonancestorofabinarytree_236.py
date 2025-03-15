# Solution for LeetCode Problem 236: Lowest Common Ancestor of a Binary Tree
# Time Complexity: O(N), where N is the number of nodes in the tree.
#   - Each node is visited once in the recursive traversal.
# Space Complexity: O(H), where H is the height of the tree.
#   - The recursive call stack takes up O(H) space, which is O(log N) for a balanced tree 
#     and O(N) for a skewed tree.

from typing import Optional

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two given nodes in a binary tree.

        The lowest common ancestor is defined as the deepest node that has both p and q
        as descendants (including itself).

        Parameters:
        root (TreeNode): The root of the binary tree.
        p (TreeNode): The first target node.
        q (TreeNode): The second target node.

        Returns:
        TreeNode: The lowest common ancestor of nodes p and q.
        """
        # Base case: If root is None or matches one of the target nodes, return root
        if not root or root.val == p.val or root.val == q.val:
            return root

        # Recursively search in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in different subtrees, root is the LCA
        if left and right:
            return root

        # If one of them is None, return the non-None value (either left or right)
        return left or right

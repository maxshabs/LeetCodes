# Solution for LeetCode Problem 872: Leaf-Similar Trees
# Time Complexity: O(N + M), where N and M are the number of nodes in root1 and root2, respectively.
#   - We perform a depth-first traversal on both trees, visiting each node once.
# Space Complexity: O(N + M), as we store the leaf values in lists.

from typing import Optional, List

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees have the same leaf sequence.

        Parameters:
        root1 (Optional[TreeNode]): The root of the first binary tree.
        root2 (Optional[TreeNode]): The root of the second binary tree.

        Returns:
        bool: True if both trees have the same leaf sequence, False otherwise.
        """
        def get_leaves(root: Optional[TreeNode], values: List[int]) -> None:
            """
            Traverses the tree using DFS and collects leaf node values.

            Parameters:
            root (Optional[TreeNode]): The root node of the current subtree.
            values (List[int]): List to store leaf values.
            """
            if not root:
                return
            
            if not root.left and not root.right:  # If it's a leaf node, add to values list
                values.append(root.val)
            
            # Recursively traverse left and right subtrees
            get_leaves(root.left, values)
            get_leaves(root.right, values)

        # Store leaf sequences for both trees
        root1_leaves = []
        root2_leaves = []

        get_leaves(root1, root1_leaves)
        get_leaves(root2, root2_leaves)

        # Compare leaf sequences
        return root1_leaves == root2_leaves

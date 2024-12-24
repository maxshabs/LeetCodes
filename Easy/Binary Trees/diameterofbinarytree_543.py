# Solution for LeetCode Problem 543: Diameter of Binary Tree
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the binary tree (due to the recursive stack space).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Computes the diameter of a binary tree. The diameter is defined as the number
        of edges in the longest path between any two nodes in the tree.
        
        :param root: The root of the binary tree.
        :return: The diameter of the binary tree.
        """
        self.result = 0  # Variable to store the maximum diameter encountered.

        def maxDepth(root: Optional[TreeNode]) -> int:
            """
            A helper function to calculate the maximum depth of a tree and update
            the diameter during traversal.
            
            :param root: The current root node being processed.
            :return: The height (depth) of the tree rooted at the current node.
            """
            if not root:
                return 0  # Base case: the height of an empty tree is 0.
            
            # Recursively calculate the depth of left and right subtrees.
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            
            # Update the diameter: the longest path through the current node.
            self.result = max(self.result, left_depth + right_depth)
            
            # Return the height of the current node.
            return 1 + max(left_depth, right_depth)
        
        # Start the depth-first search from the root.
        maxDepth(root)
        
        # The result contains the maximum diameter.
        return self.result

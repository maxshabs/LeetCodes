# Solution for LeetCode Problem 110: Balanced Binary Tree
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced. A binary tree is height-balanced
        if the depth of the two subtrees of every node never differs by more than one.
        
        :param root: The root node of the binary tree.
        :return: True if the tree is balanced, False otherwise.
        """
        def heightAndBalanced(root: Optional[TreeNode]):
            """
            A helper function that computes both the height of the tree and whether it is balanced.
            
            :param root: The current node being processed.
            :return: A list [is_balanced, height], where:
                     - is_balanced (bool): Whether the subtree rooted at this node is balanced.
                     - height (int): The height of the subtree rooted at this node.
            """
            if not root:
                return [True, 0]  # An empty tree is balanced with a height of 0.
            
            # Recursively check the left and right subtrees
            left_subtree = heightAndBalanced(root.left)
            right_subtree = heightAndBalanced(root.right)
            
            # Determine if the current node's subtree is balanced
            is_balanced = (
                abs(left_subtree[1] - right_subtree[1]) <= 1
                and left_subtree[0]
                and right_subtree[0]
            )
            
            # Compute the height of the current node's subtree
            height = 1 + max(left_subtree[1], right_subtree[1])
            
            return [is_balanced, height]
        
        # Return whether the tree is balanced
        return heightAndBalanced(root)[0]

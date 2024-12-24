# Solution for LeetCode Problem 100: Same Tree
# Time Complexity: O(n), where n is the number of nodes in the smaller of the two trees.
# Space Complexity: O(h), where h is the height of the recursion stack (the depth of the tree).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines if two binary trees are identical. Two trees are considered identical
        if they have the same structure and node values.
        
        :param p: Root of the first binary tree.
        :param q: Root of the second binary tree.
        :return: True if the trees are identical, False otherwise.
        """
        # Base Case 1: Both trees are empty.
        if not p and not q:
            return True
        
        # Base Case 2: One tree is empty, and the other is not.
        if (not p and q) or (p and not q):
            return False
        
        # Base Case 3: The values of the current nodes do not match.
        if p.val != q.val:
            return False
        
        # Recursively compare the left and right subtrees.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

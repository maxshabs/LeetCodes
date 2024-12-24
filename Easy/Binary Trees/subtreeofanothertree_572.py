# Solution for LeetCode Problem 572: Subtree of Another Tree
# Time Complexity: O(n * m), where n is the number of nodes in the `root` tree and m is the number of nodes in the `subRoot` tree.
# Space Complexity: O(h), where h is the height of the `root` tree due to the recursion stack.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determines if `subRoot` is a subtree of `root`.
        
        :param root: The root node of the main tree.
        :param subRoot: The root node of the potential subtree.
        :return: True if `subRoot` is a subtree of `root`, False otherwise.
        """
        # Base Case 1: If the `root` tree is empty, it cannot contain `subRoot`.
        if not root:
            return False
        
        # Base Case 2: An empty `subRoot` is always a subtree of any tree.
        if not subRoot:
            return True

        # Check if the current `root` and `subRoot` trees are identical.
        if self.sameTree(root, subRoot):
            return True
        
        # Recursively check the left and right subtrees of `root`.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Determines if two trees are identical.
        
        :param p: Root of the first tree.
        :param q: Root of the second tree.
        :return: True if the trees are identical, False otherwise.
        """
        # Both trees are empty.
        if not p and not q:
            return True
        
        # Both trees are non-empty, and the current nodes have the same value.
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
        # One tree is empty, or the current nodes have different values.
        return False

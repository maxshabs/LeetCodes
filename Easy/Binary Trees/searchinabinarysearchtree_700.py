# Solution for LeetCode Problem 700: Search in a Binary Search Tree
# Time Complexity: O(H), where H is the height of the tree.
#   - In the worst case (unbalanced tree), H = O(N).
#   - In the best case (balanced BST), H = O(log N).
# Space Complexity: O(H), due to recursive function calls (O(log N) for balanced trees, O(N) for skewed trees).

from typing import Optional

class TreeNode:
    """
    Definition for a binary search tree (BST) node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Searches for a node with a given value in a Binary Search Tree (BST).

        Parameters:
        root (Optional[TreeNode]): The root node of the BST.
        val (int): The value to search for.

        Returns:
        Optional[TreeNode]: The subtree rooted at the node with value `val`, or None if not found.
        """
        # Base case: If the root is None or the value matches the root
        if not root:
            return None
        
        if root.val == val:
            return root  # Found the node, return it
        
        # If the value is smaller, search in the left subtree
        if root.val > val:
            return self.searchBST(root.left, val)
        
        # If the value is larger, search in the right subtree
        return self.searchBST(root.right, val)

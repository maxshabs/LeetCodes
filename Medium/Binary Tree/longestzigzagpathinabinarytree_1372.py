# Solution for LeetCode Problem 1372: Longest ZigZag Path in a Binary Tree
# Time Complexity: O(N), where N is the number of nodes in the tree.
#   - Each node is visited once in a depth-first search (DFS).
# Space Complexity: O(H), where H is the height of the tree.
#   - This accounts for the recursive call stack, which is O(log N) for balanced trees 
#     and O(N) for a skewed tree.

from typing import Optional

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        """
        Finds the longest ZigZag path in a binary tree.
        
        A ZigZag path alternates between left and right child nodes.

        Parameters:
        root (Optional[TreeNode]): The root of the binary tree.

        Returns:
        int: The length of the longest ZigZag path.
        """
        self.max_len = 0  # Stores the maximum ZigZag path length

        def dfs(root: Optional[TreeNode], left_len: int, right_len: int) -> None:
            """
            Performs a depth-first search to compute the longest ZigZag path.

            Parameters:
            root (Optional[TreeNode]): The current node being processed.
            left_len (int): The length of the ZigZag path if coming from the left.
            right_len (int): The length of the ZigZag path if coming from the right.
            """
            if not root:
                return
            
            # Update the maximum ZigZag path length found so far
            self.max_len = max(self.max_len, left_len, right_len)

            # Recursively process the left and right children
            if root.left:
                dfs(root.left, right_len + 1, 0)  # Move left, resetting right path
            if root.right:
                dfs(root.right, 0, left_len + 1)  # Move right, resetting left path

        # Start DFS from the root with initial lengths of 0
        dfs(root, 0, 0)

        return self.max_len

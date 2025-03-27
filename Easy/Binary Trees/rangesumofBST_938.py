# Solution for LeetCode Problem 938: Range Sum of BST
# Time Complexity: O(N), where N is the number of nodes visited.
#   - In the worst case, all nodes are visited (unbalanced tree or all nodes in range).
# Space Complexity: O(H), where H is the height of the tree (due to recursion stack).
#   - Worst case O(N) for a skewed tree, O(log N) for a balanced BST.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0  # Base case: null node contributes 0 to the sum

            # If current node value is less than low, ignore left subtree
            if root.val < low:
                return dfs(root.right)

            # If current node value is greater than high, ignore right subtree
            if root.val > high:
                return dfs(root.left)

            # Current node is within range: include its value and check both subtrees
            return root.val + dfs(root.left) + dfs(root.right)
    
        return dfs(root)

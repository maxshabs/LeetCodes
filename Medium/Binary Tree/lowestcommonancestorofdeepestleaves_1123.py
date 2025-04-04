# Solution for LeetCode Problem 1123: Lowest Common Ancestor of Deepest Leaves
# Time Complexity: O(N), where N is the number of nodes in the tree.
#   - Each node is visited once in the depth-first search.
# Space Complexity: O(H), where H is the height of the tree (due to the recursion stack).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return (None, 0)  # Base case: null node has depth 0 and no LCA

            # Recursively compute LCA and depth of left and right subtrees
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            # If left is deeper, return its LCA and increased depth
            if left_depth > right_depth:
                return (left_node, left_depth + 1)
            # If right is deeper, return its LCA and increased depth
            elif right_depth > left_depth:
                return (right_node, right_depth + 1)
            else:
                # If both are equally deep, current node is the LCA
                return (node, left_depth + 1)

        # Start DFS from root and return the LCA part of the result
        lca, _ = dfs(root)
        return lca

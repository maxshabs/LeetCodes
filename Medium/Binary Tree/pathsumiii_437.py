# Solution for LeetCode Problem 437: Path Sum III
# Time Complexity: O(N), where N is the number of nodes in the binary tree.
#   - Each node is visited once in a depth-first traversal.
# Space Complexity: O(N), due to the hashmap storing prefix sums and recursive call stack.

from typing import Optional
from collections import defaultdict

class TreeNode:
    """
    Definition for a binary tree node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        Finds the number of paths in the binary tree that sum to the given targetSum.
        Paths do not have to start at the root or end at a leaf, but they must move downward.

        Parameters:
        root (Optional[TreeNode]): The root of the binary tree.
        targetSum (int): The target sum to find in the paths.

        Returns:
        int: The total number of paths that sum to targetSum.
        """
        # Hashmap to store the prefix sum frequencies
        freq = {0: 1}  # Base case: A sum of 0 exists once (important for finding exact matches)

        def dfs(root: Optional[TreeNode], cur_sum: int) -> int:
            """
            Performs a DFS traversal while maintaining the running sum and counting valid paths.

            Parameters:
            root (Optional[TreeNode]): The current node in the DFS traversal.
            cur_sum (int): The cumulative sum from the root to the current node.

            Returns:
            int: The count of valid paths ending at this node.
            """
            if not root:
                return 0
            
            cur_sum += root.val  # Update the current prefix sum
            
            # Count paths that sum to targetSum using the prefix sum technique
            paths = freq.get(cur_sum - targetSum, 0)

            # Store the current prefix sum in the hashmap
            freq[cur_sum] = freq.get(cur_sum, 0) + 1

            # Recursive DFS traversal for left and right subtrees
            paths += dfs(root.left, cur_sum)
            paths += dfs(root.right, cur_sum)

            # Backtrack: Remove the current prefix sum from the hashmap
            freq[cur_sum] -= 1

            return paths

        return dfs(root, 0)  # Start DFS with an initial cumulative sum of 0

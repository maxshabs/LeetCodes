# Solution for LeetCode Problem 1448: Count Good Nodes in Binary Tree
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(n), where n is the number of nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Counts the number of "good" nodes in a binary tree.
        
        A node X in the binary tree is considered "good" if the value of X is greater than or equal 
        to the maximum value encountered on the path from the root to X.
        
        :param root: The root node of the binary tree.
        :return: The number of "good" nodes in the tree.
        """
        if not root:
            return 0
        
        def dfs(root: TreeNode, max_so_far: int) -> int:
            """
            Depth-first search (DFS) to traverse the tree and count good nodes.
            
            :param root: The current node in the tree.
            :param max_so_far: The maximum value encountered from the root to the current node.
            :return: The number of good nodes in the subtree rooted at the current node.
            """
            if not root:
                return 0
            
            # Check if the current node is a "good" node
            if root.val >= max_so_far:
                res = 1
                max_so_far = max(root.val, max_so_far)  # Update max_so_far
            else:
                res = 0
            
            # Recur for the left and right subtrees
            res += dfs(root.left, max_so_far)
            res += dfs(root.right, max_so_far)
            
            return res
        
        # Start DFS from the root with its value as the initial max_so_far
        return dfs(root, root.val)

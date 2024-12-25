# Solution for LeetCode Problem 230: Kth Smallest Element in a BST
# Time Complexity: O(n), where n is the number of nodes in the BST. 
# In the worst case, the algorithm might visit all nodes in the tree.
# Space Complexity: O(h), where h is the height of the BST, due to the stack used for in-order traversal.

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the kth smallest element in a Binary Search Tree (BST).
        
        :param root: The root of the BST.
        :param k: The target rank of the smallest element (1-based index).
        :return: The value of the kth smallest element in the BST.
        """
        count = 0  # Counter to track the rank of the current node during in-order traversal
        node_stack = []  # Stack to facilitate the iterative in-order traversal
        cur = root  # Pointer to the current node being processed
        
        while cur or node_stack:
            # Traverse to the leftmost node
            while cur:
                node_stack.append(cur)
                cur = cur.left
            
            # Process the current node
            cur = node_stack.pop()
            count += 1
            # If the current node is the kth smallest, return its value
            if count == k:
                return cur.val
            
            # Move to the right subtree
            cur = cur.right

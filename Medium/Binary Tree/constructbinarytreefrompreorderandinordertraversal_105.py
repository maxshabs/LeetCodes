# Solution for LeetCode Problem 105: Construct Binary Tree from Preorder and Inorder Traversal
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(n), due to the additional space required for the `indices_dict` and the recursion stack.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from its preorder and inorder traversal arrays.
        
        :param preorder: A list of integers representing the preorder traversal of the tree.
        :param inorder: A list of integers representing the inorder traversal of the tree.
        :return: The root of the constructed binary tree.
        """
        # Create a dictionary to map values in the inorder list to their indices for quick lookup
        self.indices_dict = {value: index for index, value in enumerate(inorder)}
        
        # Pointer to track the current index in the preorder traversal
        self.preorder_index = 0

        def dfs(left: int, right: int) -> Optional[TreeNode]:
            """
            Recursive function to construct the binary tree.
            
            :param left: The start index of the current subtree in the inorder list.
            :param right: The end index of the current subtree in the inorder list.
            :return: The root node of the constructed subtree.
            """
            # Base Case: If the range is invalid, return None
            if left > right:
                return None
            
            # Get the current root value from preorder
            val = preorder[self.preorder_index]
            self.preorder_index += 1
            
            # Create the root node with the current value
            cur_node = TreeNode(val)
            
            # Get the index of the root value in the inorder list
            cur_index = self.indices_dict[val]
            
            # Recursively construct the left and right subtrees
            cur_node.left = dfs(left, cur_index - 1)
            cur_node.right = dfs(cur_index + 1, right)
            
            return cur_node

        # Construct the binary tree starting with the entire range of the inorder list
        return dfs(0, len(preorder) - 1)

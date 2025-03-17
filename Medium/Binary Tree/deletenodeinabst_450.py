# Solution for LeetCode Problem 450: Delete Node in a BST
# Time Complexity: O(H), where H is the height of the BST.
#   - In the worst case (unbalanced BST), H = O(N).
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node with the given key from a Binary Search Tree (BST).

        Parameters:
        root (Optional[TreeNode]): The root of the BST.
        key (int): The value of the node to be deleted.

        Returns:
        Optional[TreeNode]: The root of the modified BST after deletion.
        """
        if not root:
            return None  # Base case: If the tree is empty or key is not found

        # Search for the node to be deleted
        if root.val > key:
            root.left = self.deleteNode(root.left, key)  # Search in the left subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)  # Search in the right subtree
        else:
            # Node with only one child or no child
            if not root.left:
                return root.right  # Replace with right child
            elif not root.right:
                return root.left  # Replace with left child

            # Node with two children: Find the inorder successor (smallest in the right subtree)
            temp = root.right
            while temp.left:
                temp = temp.left  # Find the leftmost node in right subtree

            # Replace the root's value with the inorder successor's value
            root.val = temp.val

            # Delete the inorder successor node from the right subtree
            root.right = self.deleteNode(root.right, temp.val)

        return root  # Return the modified root after deletion

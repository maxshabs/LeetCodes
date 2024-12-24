# Solution for LeetCode Problem 235: Lowest Common Ancestor of a Binary Search Tree
# Time Complexity: O(h), where h is the height of the binary search tree.
# Space Complexity: O(1), as no additional space is used other than a single pointer.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two nodes, p and q, in a Binary Search Tree (BST).
        
        :param root: The root node of the BST.
        :param p: The first target node.
        :param q: The second target node.
        :return: The lowest common ancestor of nodes p and q.
        """
        search_node = root  # Start from the root of the BST.

        while True:
            # If both p and q are smaller than the current node, traverse to the left subtree.
            if search_node.val > p.val and search_node.val > q.val:
                search_node = search_node.left
            # If both p and q are greater than the current node, traverse to the right subtree.
            elif search_node.val < p.val and search_node.val < q.val:
                search_node = search_node.right
            # If p and q are on opposite sides of the current node, or one of them is equal to the current node,
            # then the current node is the LCA.
            else:
                return search_node

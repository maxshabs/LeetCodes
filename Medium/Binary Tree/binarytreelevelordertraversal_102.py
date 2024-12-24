# Solution for LeetCode Problem 102: Binary Tree Level Order Traversal
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(n), where n is the number of nodes in the binary tree.

from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs level order traversal on a binary tree.
        
        :param root: Root node of the binary tree.
        :return: A list of lists, where each inner list contains the values of the nodes at that level.
        """
        q = deque()  # Queue for BFS traversal
        if root:
            q.append(root)  # Initialize the queue with the root node
        ret_list = []  # Final result list to store values level by level
        
        while q:
            q_len = len(q)  # Number of nodes at the current level
            cur_list = []  # List to store the values of nodes at the current level
            
            for i in range(q_len):
                node = q.popleft()  # Dequeue the front node
                cur_list.append(node.val)  # Add the node's value to the current level list
                
                # Enqueue the left and right children, if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if cur_list:
                ret_list.append(cur_list)  # Append the current level list to the result list
        
        return ret_list

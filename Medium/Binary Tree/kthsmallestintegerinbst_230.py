from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        node_stack = []
        cur = root
        
        while cur and node_stack:
            while cur:
                node_stack.append(cur)
                cur = cur.left
            
            cur = node_stack.pop()
            count += 1
            if count == k:
                return cur.val

            cur = cur.right
        
                
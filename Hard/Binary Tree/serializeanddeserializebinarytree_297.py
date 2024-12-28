# Solution for LeetCode Problem 297: Serialize and Deserialize Binary Tree
# Time Complexity:
# - `serialize`: O(n), where n is the number of nodes in the binary tree. Each node is visited once during breadth-first traversal.
# - `deserialize`: O(n), where n is the number of values in the serialized string. Each value is processed to reconstruct the tree.
# Space Complexity: O(n)
# - The space used by the queue in both `serialize` and `deserialize` is proportional to the number of nodes in the tree.

from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a binary tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Step 1: Edge case for an empty tree
        if not root:
            return ""

        # Step 2: Initialize the queue for BFS and the result string
        ret_str = ""
        node_queue = deque([root])

        # Step 3: Perform level-order traversal (BFS)
        while node_queue:
            cur_node = node_queue.popleft()
            if cur_node:
                # Append node value to the serialized string
                ret_str += f"{cur_node.val}#"
                # Add left and right children to the queue
                node_queue.append(cur_node.left)
                node_queue.append(cur_node.right)
            else:
                # Append placeholder for null nodes
                ret_str += "N#"

        return ret_str

    def deserialize(self, data):
        """
        Decodes a serialized string back to a binary tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Step 1: Edge case for empty string
        if not data:
            return None

        # Step 2: Split the serialized string into node values
        vals = data.split("#")[:-1]  # Remove the trailing empty value after the split

        # Step 3: Initialize the root and the queue for BFS
        root = TreeNode(int(vals[0]))
        node_queue = deque([root])
        j = 1

        # Step 4: Reconstruct the tree level by level
        while node_queue:
            cur_node = node_queue.popleft()
            # Process the left child
            if vals[j] != "N":
                cur_node.left = TreeNode(int(vals[j]))
                node_queue.append(cur_node.left)
            j += 1
            # Process the right child
            if vals[j] != "N":
                cur_node.right = TreeNode(int(vals[j]))
                node_queue.append(cur_node.right)
            j += 1

        return root

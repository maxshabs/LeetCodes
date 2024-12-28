from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        ret_str = ""
        if not root:
            return ""
        node_queue = deque()
        node_queue.append(root)
        while node_queue:
            q_len = len(node_queue)
            i = 0
            while i < q_len:
                cur_node = node_queue.popleft()
                i += 1
                if cur_node:
                    ret_str += f"{cur_node.val}#"
                else:
                    ret_str += "N#"
                    continue
                
                node_queue.append(cur_node.left)
                node_queue.append(cur_node.right)
        
        return ret_str
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        vals = data.split("#")
        node_queue = deque()
        root = TreeNode(vals[0])
        node_queue.append(root)
        j = 1
        while node_queue:
            cur_node = node_queue.popleft()
            if vals[j] != "N":
                cur_node.left = TreeNode(vals[j])
                node_queue.append(cur_node.left)
            j += 1
            if vals[j] != "N":
                cur_node.right = TreeNode(vals[j])
                node_queue.append(cur_node.right)
            j += 1

        return root

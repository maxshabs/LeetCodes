# Solution for LeetCode Problem 19: Remove Nth Node From End of List
# Time Complexity: O(n), where n is the number of nodes in the linked list.
#   - The first traversal counts the nodes in the list, taking O(n).
#   - The second traversal removes the nth node, taking O(n).
# Space Complexity: O(1), as the operation is performed in-place without additional data structures.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a singly linked list.

        :param head: Optional[ListNode] - The head of the singly linked list.
        :param n: int - The position (from the end) of the node to remove.
        :return: Optional[ListNode] - The head of the modified linked list.
        """
        # Step 1: Count the total number of nodes
        cur_node = head
        nodes_num = 0
        while cur_node:
            cur_node = cur_node.next
            nodes_num += 1
        
        # Step 2: Handle the case where the head needs to be removed
        cur_node = head
        if nodes_num - n == 0:
            return head.next
            
        # Step 3: Traverse again to find the (n-1)th node and remove the nth node
        counter = 0
        while cur_node:
            counter += 1
            if counter == nodes_num - n:
                if cur_node.next.next:
                    cur_node.next = cur_node.next.next  # Link to the node after the nth node
                else:
                    cur_node.next = None  # If nth node is the last node, set next to None
            cur_node = cur_node.next
                    
        return head

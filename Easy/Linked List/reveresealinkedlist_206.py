# Solution for LeetCode Problem 206: Reverse Linked List
# Time Complexity: O(n), where n is the number of nodes in the linked list.
#   - Each node is visited exactly once during the traversal.
# Space Complexity: O(1), as no additional data structures are used apart from a few variables.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers
        cur_node = head        # Pointer to the current node being processed
        prev_node = None       # Pointer to the previous node in the reversed list
        
        # Traverse the list and reverse the links
        while cur_node is not None:
            next_node = cur_node.next  # Store the next node temporarily
            cur_node.next = prev_node  # Reverse the link
            prev_node = cur_node       # Move the previous pointer forward
            cur_node = next_node       # Move the current pointer forward

        # At the end, prev_node points to the new head of the reversed list
        return prev_node

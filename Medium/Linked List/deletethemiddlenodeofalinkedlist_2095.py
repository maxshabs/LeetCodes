# Solution for LeetCode Problem 2095: Delete the Middle Node of a Linked List
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#   - We traverse the linked list once using the two-pointer technique.
# Space Complexity: O(1), as we modify the list in place without using extra space.

from typing import Optional

class ListNode:
    """
    Definition for a singly-linked list node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes the middle node of a singly linked list.

        Parameters:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        Optional[ListNode]: The head of the linked list after deleting the middle node.
        """
        # Edge case: If there is only one node, return None (delete the only node)
        if not head or not head.next:
            return None

        prev = ListNode(-1)  # Dummy node to handle edge cases
        prev.next = head
        slow = prev  # Slow pointer (will stop before the middle node)
        fast = head  # Fast pointer (moves twice as fast)

        # Move fast pointer two steps at a time, slow pointer one step at a time
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Delete the middle node by skipping it in the linked list
        slow.next = slow.next.next

        return head  # Return the modified head of the list

# Solution for LeetCode Problem 141: Linked List Cycle
# Time Complexity: O(n), where n is the number of nodes in the linked list.
#   - Each node is visited at most twice: once by the `slow` pointer and once by the `fast` pointer.
# Space Complexity: O(1), as only two pointers are used regardless of the size of the linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle. A cycle exists if a node's `next`
        pointer points to a previous node in the list.

        :param head: Optional[ListNode] - The head of the linked list.
        :return: bool - True if the list contains a cycle, False otherwise.
        """
        # If the linked list is empty or has only one node, it cannot have a cycle
        if not head:
            return False

        # Initialize two pointers: `slow` and `fast`
        slow, fast = head, head.next

        # Traverse the list with the two pointers
        while fast and fast.next:
            # If the `fast` pointer meets the `slow` pointer, a cycle is detected
            if fast == slow:
                return True
            # Move the `fast` pointer two steps ahead
            fast = fast.next.next
            # Move the `slow` pointer one step ahead
            slow = slow.next

        # If the `fast` pointer reaches the end of the list, no cycle exists
        return False

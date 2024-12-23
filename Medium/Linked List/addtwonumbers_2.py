# Solution for LeetCode Problem 2: Add Two Numbers
# Time Complexity: O(max(m, n)), where m and n are the lengths of the two input linked lists.
#   - The loop iterates through the longer of the two linked lists.
# Space Complexity: O(max(m, n)), as the resulting linked list can have at most one extra node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented as linked lists. Each node contains a single digit,
        and the digits are stored in reverse order. Returns a linked list representing
        the sum of the two numbers, also in reverse order.

        :param l1: Optional[ListNode] - The head of the first linked list.
        :param l2: Optional[ListNode] - The head of the second linked list.
        :return: Optional[ListNode] - The head of the resulting linked list.
        """
        # Initialize pointers for traversing the input lists
        cur_l1 = l1  # Read-only pointer for the first list
        cur_l2 = l2  # Read-only pointer for the second list

        # Initialize a dummy node for the resulting linked list
        res_node = res_list = ListNode(-1)

        # Initialize the carry for summing digits
        carry = 0

        # Step 1: Add digits while there are nodes in either list
        while cur_l1 or cur_l2:
            val1 = cur_l1.val if cur_l1 else 0  # Value from the first list, or 0 if it's None
            val2 = cur_l2.val if cur_l2 else 0  # Value from the second list, or 0 if it's None

            # Calculate the current value and the carry
            cur_val = val1 + val2 + carry
            carry = 1 if cur_val >= 10 else 0  # Update carry
            res_node.next = ListNode(cur_val % 10)  # Add the remainder as a new node

            # Move the result pointer forward
            res_node = res_node.next

            # Move to the next nodes in the input lists (if they exist)
            if cur_l1:
                cur_l1 = cur_l1.next
            if cur_l2:
                cur_l2 = cur_l2.next

        # Step 2: Handle any remaining carry
        if carry == 1:
            res_node.next = ListNode(1)

        # Return the resulting linked list, skipping the dummy node
        return res_list.next

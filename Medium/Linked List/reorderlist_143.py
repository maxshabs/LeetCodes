# Solution for LeetCode Problem 143: Reorder List
# Time Complexity: O(n), where n is the number of nodes in the linked list.
#   - Finding the middle of the list takes O(n).
#   - Reversing the second half takes O(n).
#   - Merging the two halves takes O(n).
# Space Complexity: O(1), as all operations are done in-place without using extra space.

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find the middle of the list using the two-pointer technique
        jump = double_jump = head
        while double_jump and double_jump.next:
            jump = jump.next  # Move one step
            double_jump = double_jump.next.next  # Move two steps

        # Step 2: Reverse the second half of the list starting from the middle
        reverse_ptr = jump.next
        prev = None
        jump.next = None  # Split the list into two halves
        while reverse_ptr:
            temp = reverse_ptr.next  # Store the next node
            reverse_ptr.next = prev  # Reverse the link
            prev = reverse_ptr  # Move prev pointer forward
            reverse_ptr = temp  # Move reverse_ptr pointer forward

        # Step 3: Merge the two halves of the list
        normal_list, reverse_ptr = head, prev
        while reverse_ptr:
            temp1, temp2 = normal_list.next, reverse_ptr.next  # Store the next nodes
            normal_list.next = reverse_ptr  # Link a node from the reversed half
            reverse_ptr.next = temp1  # Link the next node from the original half
            reverse_ptr = temp2  # Move the reversed half pointer forward
            normal_list = temp1  # Move the original half pointer forward

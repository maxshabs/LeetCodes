# Solution for LeetCode Problem 138: Copy List with Random Pointer
# Time Complexity: O(n), where n is the number of nodes in the linked list.
#   - First pass: Create deep copies and interweave them with the original nodes.
#   - Second pass: Update the `random` pointers of the new nodes.
#   - Third pass: Separate the original list from the deep copy.
# Space Complexity: O(1), as no additional data structures are used (the deep copy is constructed in-place).

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Creates a deep copy of a linked list where each node has a random pointer.
        The algorithm works in three steps:
        1. Interweaving copied nodes with the original list.
        2. Assigning the `random` pointers for the copied nodes.
        3. Separating the original list and the copied list.

        :param head: Optional[Node] - The head of the original linked list.
        :return: Optional[Node] - The head of the deep-copied linked list.
        """
        if head is None:
            return None

        # Step 1: Create interwoven linked list with copied nodes
        l1 = head
        while l1:
            l2 = Node(l1.val)  # Create a copy of the current node
            l2.next = l1.next  # Point the copy's next to the original's next
            l1.next = l2       # Insert the copy after the original
            l1 = l2.next       # Move to the next original node

        # Step 2: Assign `random` pointers for the copied nodes
        newHead = head.next  # The copied list's head
        l1 = head
        while l1:
            if l1.random:  # If the original node has a `random` pointer
                l1.next.random = l1.random.next  # Assign the copy's `random` pointer
            l1 = l1.next.next  # Move to the next original node

        # Step 3: Separate the copied list from the original list
        l1 = head
        while l1:
            l2 = l1.next          # Copy node
            l1.next = l2.next     # Restore the original list's `next` pointer
            if l2.next:           # If there's a next node in the copied list
                l2.next = l2.next.next  # Point the copy's `next` to the next copied node
            l1 = l1.next          # Move to the next original node

        return newHead

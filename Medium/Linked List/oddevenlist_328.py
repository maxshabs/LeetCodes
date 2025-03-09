# Solution for LeetCode Problem 328: Odd Even Linked List
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#   - We traverse the list once, reordering nodes in-place.
# Space Complexity: O(1), as we modify the list without extra space.

from typing import Optional

class ListNode:
    """
    Definition for a singly-linked list node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Groups nodes in the linked list such that all odd-indexed nodes appear before even-indexed nodes.

        Parameters:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        Optional[ListNode]: The head of the modified linked list.
        """
        # Edge case: If the list is empty, return None
        if not head:
            return None
            
        odd = head  # Pointer for the last odd-indexed node
        even = head.next  # Pointer for the last even-indexed node
        e_head = even  # Store the head of the even-indexed nodes
        
        # Traverse the list, separating odd and even indexed nodes
        while even and even.next:
            odd.next = odd.next.next  # Skip the next even node
            even.next = even.next.next  # Skip the next odd node
            
            odd = odd.next  # Move odd pointer forward
            even = even.next  # Move even pointer forward
        
        # Connect the last odd node to the first even node
        odd.next = e_head

        return head  # Return the modified head of the list

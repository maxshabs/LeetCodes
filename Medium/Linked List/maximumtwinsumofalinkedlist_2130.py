# Solution for LeetCode Problem 2130: Maximum Twin Sum of a Linked List
# Time Complexity: O(N), where N is the number of nodes in the linked list.
#   - Finding the middle of the list takes O(N).
#   - Reversing the first half takes O(N).
#   - Computing the twin sums takes O(N).
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
    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        Finds the maximum twin sum of the linked list, where twin nodes are equidistant 
        from the start and end of the list.

        Parameters:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        int: The maximum twin sum found in the list.
        """
        slow, fast = head, head
        new_list = None  # Reversed first half of the list

        # Step 1: Find the middle of the linked list while reversing the first half
        while fast and fast.next:
            fast = fast.next.next  # Move fast pointer twice as fast
            temp = slow.next  # Store next node
            slow.next = new_list  # Reverse the link for the first half
            new_list = slow  # Move new_list pointer
            slow = temp  # Move slow pointer

        # Step 2: Compute twin sums using the reversed first half and second half
        max_sum = 0
        while slow:
            max_sum = max(max_sum, slow.val + new_list.val)  # Compute twin sum
            slow = slow.next  # Move forward in the second half
            new_list = new_list.next  # Move forward in the reversed first half
        
        return max_sum  # Return the maximum twin sum

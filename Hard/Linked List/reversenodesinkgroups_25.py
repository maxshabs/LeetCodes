# Solution for LeetCode Problem 25: Reverse Nodes in k-Group
# Time Complexity: O(n), where n is the number of nodes in the linked list.
#   - Each node is processed exactly once, either for counting or reversal.
# Space Complexity: O(1) additional space, as the reversal is done in place.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes of the linked list in groups of size k. If the number of nodes remaining 
        is less than k, they remain in the same order.

        :param head: The head of the linked list.
        :param k: The size of groups to reverse.
        :return: The head of the modified linked list.
        """
        if not head or k == 1:
            return head  # No reversal needed for empty list or k=1

        # Dummy node to simplify edge cases, such as reversing the first group
        dummy = ListNode(-1, head)
        left = dummy

        while True:
            # Find the kth node from `left` to determine the group to reverse
            current_count = 0
            right = left
            while current_count < k and right.next:
                right = right.next
                current_count += 1
            
            # If there are fewer than k nodes remaining, exit the loop
            if current_count < k:
                break
            
            # Reverse the k nodes
            prev = None
            current_node = left.next
            for _ in range(k):
                temp = current_node.next  # Temporarily store the next node
                current_node.next = prev  # Reverse the link
                prev = current_node  # Move `prev` forward
                current_node = temp  # Move `current_node` forward
            
            # Update the connections to maintain the list structure
            next_group = left.next  # Save the first node of the current group (now the last)
            next_group.next = current_node  # Connect the last node of the reversed group to the next node
            left.next = prev  # Connect the previous group to the new head of the reversed group
            
            # Move `left` to the end of the current group for the next iteration
            left = next_group
        
        # Return the new head of the linked list
        return dummy.next

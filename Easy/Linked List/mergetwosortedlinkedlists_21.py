# Solution for LeetCode Problem 21: Merge Two Sorted Lists
# Time Complexity: O(n + m), where n and m are the lengths of the two linked lists.
#   - Each node in both linked lists is processed exactly once.
# Space Complexity: O(1), as the merging is performed in-place without using additional data structures.

from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(-1)
        current = dummy  # Pointer to the current node in the merged list

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move the pointer forward

        # Attach the remaining nodes, if any
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # The merged list starts at dummy.next
        return dummy.next

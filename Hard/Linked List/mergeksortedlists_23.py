# Solution for LeetCode Problem 23: Merge k Sorted Lists
# Time Complexity: O(N log k), where N is the total number of nodes in all lists and k is the number of linked lists.
#   - The merging of two lists takes O(N) time in total, and there are log k levels of merging.
# Space Complexity: O(1) additional space (excluding recursion stack for list nodes), since merging is done in place.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List

class Solution:
    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into one sorted linked list.

        :param list1: Optional[ListNode] - The head of the first sorted linked list.
        :param list2: Optional[ListNode] - The head of the second sorted linked list.
        :return: Optional[ListNode] - The head of the merged sorted linked list.
        """
        current = head = ListNode()  # Dummy node to simplify merging logic
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: 
                current.next = list2
                list2 = list2.next
            current = current.next  # Move to the next node in the merged list
        
        # Append the remaining nodes of the non-empty list
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        return head.next  # Return the merged list, skipping the dummy node
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into one sorted linked list using iterative pairwise merging.

        :param lists: List[Optional[ListNode]] - A list of k sorted linked lists.
        :return: Optional[ListNode] - The head of the merged sorted linked list.
        """
        if len(lists) == 0:
            return None  # No lists to merge
        
        # Iteratively merge the lists two at a time until one list remains
        while len(lists) > 1:
            mergedLists = []  # Holds the merged lists after each iteration
            for i in range(0, len(lists), 2):
                # Get the second list if it exists, otherwise pass None
                second_list = lists[i + 1] if i + 1 < len(lists) else None
                # Merge the two lists
                mergedList = self.merge2Lists(lists[i], second_list)
                # Add the merged list to the merged lists
                mergedLists.append(mergedList)
            lists = mergedLists  # Update the lists with the merged results
        
        return lists[0]  # Return the final merged list

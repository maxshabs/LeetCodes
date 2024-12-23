from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        res_node = res_list = ListNode(-1)
        carry = 0
        while cur_l1 and cur_l2:
            cur_val = cur_l1.val + cur_l2.val + carry
            if cur_val >= 10:
                carry = 1
            else:
                carry = 0
            res_node.next = ListNode(cur_val % 10)
            res_node = res_node.next
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
        
        while cur_l1 and not cur_l2:
            cur_val = cur_l1.val + carry
            if cur_val >= 10:
                carry = 1
            else:
                carry = 0
            res_node.next = ListNode(cur_val % 10)
            res_node = res_node.next
            cur_l1 = cur_l1.next
        while not cur_l1 and cur_l2:
            cur_val = cur_l2.val + carry
            if cur_val >= 10:
                carry = 1
            else:
                carry = 0
            res_node.next = ListNode(cur_val % 10)
            res_node = res_node.next
            cur_l2 = cur_l2.next
            
        if carry == 1:
            res_node.next = ListNode(1)
        
        return res_list.next
            
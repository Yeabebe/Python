# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy head for result linked list
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Get values from l1 and l2, or 0 if None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add values and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create a new node with the digit
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

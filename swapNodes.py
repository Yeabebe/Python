
from typing import Optional
from AddTwoNumbers import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)   # Dummy node before head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            # Swapping
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev two steps ahead
            prev = first
        
        return dummy.next

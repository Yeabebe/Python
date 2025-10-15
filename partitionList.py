from typing import Optional
from typing import ListNode

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Dummy nodes for two partitions
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        before = before_head
        after = after_head
        current = head
        
        # Traverse and divide nodes
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next
        
        # End the after list and connect two parts
        after.next = None
        before.next = after_head.next
        
        return before_head.next

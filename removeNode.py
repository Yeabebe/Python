# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Create a dummy node before head
        first = dummy
        second = dummy        
        # Move first n+1 steps ahead so the gap is n between first and second
        for _ in range(n + 1):
            first = first.next        
        # Move both until first hits the end
        while first:
            first = first.next
            second = second.next        
        # Remove the target node
        second.next = second.next.next
        
        return dummy.next

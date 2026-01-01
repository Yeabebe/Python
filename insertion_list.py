class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)   # dummy head for sorted list
        curr = head
        
        while curr:
            prev = dummy
            nxt = curr.next   # save next node
            
            # find insertion position
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            curr.next = prev.next
            prev.next = curr
            
            curr = nxt
        
        return dummy.next
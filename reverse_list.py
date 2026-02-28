class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next   # 1. save next
            curr.next = prev        # 2. reverse pointer
            prev = curr             # 3. move prev
            curr = next_node        # 4. move curr
        
        return prev
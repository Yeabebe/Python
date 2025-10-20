class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        nxt = None

        for _ in range(right - left):
            nxt = current.next
            current.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next
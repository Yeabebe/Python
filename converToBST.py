class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMiddle(start):
            prev = None
            slow = fast = start
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            if prev:
                prev.next = None
            return slow
        if not head:
            return None
        mid = findMiddle(head)
        root = TreeNode(mid.val)
        
        if head == mid:
            return root

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root
        
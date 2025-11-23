from typing import Node

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        curr = root
        while curr:
            dummy = Node(0)
            prev = dummy

            while curr:
                if curr.left:
                    prev.next = curr.left
                    prev = prev.next
                if curr.right:
                    prev.next = curr.right
                    prev = prev.next
                curr = curr.next
            curr = dummy.next
        return root

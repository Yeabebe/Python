from typing import Optional, Node 

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        if root.left:
            root.left.next = root.right

            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

        return root
        
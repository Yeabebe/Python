class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            dfs(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node
        dfs(root)

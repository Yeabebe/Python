from typing import Optional, TreeNode

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, current):
            if not node:
                return 0
            
            # build the number
            current = current * 10 + node.val
            
            # if leaf, return the number formed
            if not node.left and not node.right:
                return current
            
            # sum from left and right subtrees
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)

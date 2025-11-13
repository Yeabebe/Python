class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.right and not root.left:
            return targetSum == root.val

        return (self.hasPathSum(root.right, targetSum - root.val) or 
                self.hasPathSum(root.left, targetSum - root.val))
        
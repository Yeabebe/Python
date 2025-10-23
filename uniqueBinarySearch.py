from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        from functools import lru_cache
        @lru_cache(None)
        def build_trees(start, end):
            if start > end:
                return [None]

            all_trees = []
            for root_val in range(start, end + 1):
                left_trees = build_trees(start, root_val - 1)
                right_trees = build_trees(root_val + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        all_trees.append(root)

            return all_trees
        return build_trees(1, n)
        
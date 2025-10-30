from collections import deque, Optional, TreeNode, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True  # direction flag

        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # reverse the level if direction is right-to-left
            if not left_to_right:
                level_nodes.reverse()

            result.append(level_nodes)
            left_to_right = not left_to_right  # flip the direction

        return result

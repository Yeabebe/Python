from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, k, target, path):
            if k == 0 and target == 0:
                res.append(path[:])
                return
            if k == 0 or target < 0:
                return

            for i in range(start, 10):
                path.append(i)
                backtrack(i + 1, k - 1, target - i, path)
                path.pop()

        backtrack(1, k, n, [])
        return res
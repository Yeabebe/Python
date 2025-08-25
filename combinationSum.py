from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            # Base case: if total == target, we found a valid combination
            if total == target:
                res.append(path[:])
                return
            # If total exceeds, stop exploring
            if total > target:
                return

            # Explore candidates starting from 'start' 
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                # Backtrack 
                path.pop()

        backtrack(0, [], 0)
        return res

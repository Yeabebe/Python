class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # sort so we can skip duplicates easily

        def backtrack(start, target, path):
            if target == 0:  # found a valid combination
                res.append(path[:])
                return
            if target < 0:  # overshoot
                return

            for i in range(start, len(candidates)):
                # skip duplicates (only if i > start)
                if i > start and candidates[i] == candidates[i-1]:
                    continue  

                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path) 
                path.pop()  # undo choice

        backtrack(0, target, [])
        return res
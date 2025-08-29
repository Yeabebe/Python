from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        
        res = []
        for i in range(len(nums)):
            n = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for perm in self.permute(remaining):
                res.append([n] + perm)
        return res

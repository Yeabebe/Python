from typing import List 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, jump in enumerate(nums):
            if i > farthest:  # we are stuck, can't reach this position
                return False
            farthest = max(farthest, i + jump)
        return True

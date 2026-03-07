from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def rob_line(houses):
            prev1 = 0
            prev2 = 0

            for money in houses:
                temp = prev1
                prev1 = max(prev1, prev2 + money)
                prev2 = temp

            return prev1

        return max(
            rob_line(nums[:-1]),  # exclude last
            rob_line(nums[1:])    # exclude first
        )
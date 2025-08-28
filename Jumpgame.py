class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        end = 0

        for i in range(len(nums) - 1):  
            farthest = max(farthest, i + nums[i])  # update farthest reach
            if i == end: 
                jumps += 1
                end = farthest  # extend the boundary

        return jumps

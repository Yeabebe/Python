from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []
        
        for i in range(n - 3):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Prune: smallest possible sum with nums[i] too large
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Prune: largest possible sum with nums[i] too small
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Prune similarly for j
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s < target:
                        left += 1
                    elif s > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        # skip duplicates for left and right
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        
        return res

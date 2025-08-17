class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # if array is empty
            return 0

        k = 1  

        # Start from the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  
                nums[k] = nums[i]  
                k += 1

        return k

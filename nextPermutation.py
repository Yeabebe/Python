class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        
        #find the pivot (first decreasing element)
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:  
            j = n - 1
            # find element just larger than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            # swap pivot and element
            nums[i], nums[j] = nums[j], nums[i]
        
        # reverse suffix (to get smallest lexicographical order)
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
